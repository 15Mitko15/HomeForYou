export class HTTPError extends Error {}
export class AuthError extends HTTPError {}
export class NotFoundError extends HTTPError {}
export class ServerError extends Error {}
export class BadRequestError extends HTTPError {}
export class ValidationError extends Error {
  constructor(
    public fieldErrors: Record<string, string[]>,
    public formErrors: []
  ) {
    super();
  }
}
export class TerritoryNotFoundError extends Error {}
export class NoFreeTerritoryError extends Error {}
