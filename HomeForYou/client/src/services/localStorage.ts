export class LocalStorageServer<T> {
  constructor(private key: string) {}

  get() {
    const value = localStorage.getItem(this.key);

    if (!value) {
      return undefined;
    }

    return this.safeParseJson(value) as T;
  }

  set(value: T) {
    localStorage.setItem(this.key, JSON.stringify(value));
  }

  clear() {
    localStorage.removeItem(this.key);
  }

  private safeParseJson(value: string) {
    try {
      return JSON.parse(value);
    } catch {
      this.clear();
    }
  }
}
