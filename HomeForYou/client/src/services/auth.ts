import { AuthError } from "../errors";
import { http } from "./http";
import { userInfoService } from "./userInfo";

export interface RegisterAttributes {
  name: string;
  email: string;
  password: string;
}

class AuthService {
  async register(body: RegisterAttributes) {
    await http.post("/auth/register", { body });
  }

  async googleLogin(authorizationCode: string) {
    await this.login(() =>
      http.post("/auth/login", { body: { authorizationCode } })
    );
  }

  async guestLogin() {
    await this.login(() => http.post("/auth/guest", {}));
  }

  logout() {
    userInfoService.clear();
  }

  private async login(
    loadHeaders: () => Promise<{
      headers: Headers;
    }>
  ) {
    const { headers } = await loadHeaders();

    const bearerToken = headers.get("authorization");

    if (!bearerToken) {
      throw new AuthError();
    }

    this.saveToken(bearerToken);
  }

  private saveToken(bearerToken: string) {
    const token = bearerToken?.replace("Bearer ", "");
    userInfoService.save(token);
  }
}

export const authService = new AuthService();
