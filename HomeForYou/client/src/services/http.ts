import { config } from "../config";
import {
  AuthError,
  BadRequestError,
  HTTPError,
  NotFoundError,
  ServerError,
  ValidationError,
} from "../errors";
import { authService } from "./auth";
import { userInfoService } from "./userInfo";

type RequestMethod = "GET" | "POST" | "PUT" | "DELETE";

interface HTTPOptions {
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  query?: Record<string, any>;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  headers?: Record<string, any>;
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  body?: Record<string, any>;
}

type GetHTTPOptions = Omit<HTTPOptions, "body">;

class HTTPService {
  get<T>(path: string, options: GetHTTPOptions) {
    return this.request<T>(path, "GET", options);
  }

  post<T>(path: string, options: HTTPOptions) {
    return this.request<T>(path, "POST", options);
  }

  put<T>(path: string, options: HTTPOptions) {
    return this.request<T>(path, "PUT", options);
  }

  delete<T>(path: string, options: HTTPOptions) {
    return this.request<T>(path, "DELETE", options);
  }

  private async request<T>(
    path: string,
    method: RequestMethod,
    { query, headers, body }: HTTPOptions
  ) {
    const token = userInfoService.authToken;

    const baseUrl = config.server.baseUrl.replace(/\/$/, "");
    const requestPath = path.replace(/^\//, "");
    const searchParams = new URLSearchParams(query).toString();

    const reqUrl = `${baseUrl}/${requestPath}?${searchParams}`;

    let res: Response;
    try {
      res = await fetch(reqUrl, {
        method,
        headers: {
          ...(token ? { Authorization: token } : {}),
          ...(body ? { "Content-Type": "application/json" } : {}),
          ...headers,
        },
        ...(body ? { body: JSON.stringify(body) } : {}),
      });
    } catch {
      throw new HTTPError();
    }

    if (!res.ok) {
      if (res.status === 400) {
        const data = await res.json();
        if ("fieldErrors" in data && "formErrors" in data) {
          throw new ValidationError(data.fieldErrors, data.formErrors);
        }
        throw new BadRequestError();
      }
      if (res.status === 401) {
        authService.logout();
        throw new AuthError();
      }
      if (res.status === 404) {
        throw new NotFoundError();
      }
      throw new ServerError();
    }

    const result = (await res.json()) as T;
    return { result, headers: res.headers };
  }
}

export const http = new HTTPService();
