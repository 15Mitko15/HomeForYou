import { Navigate, Outlet } from "react-router-dom";
import { useCurrentUser } from "../contexts/CurrentUser";

export function PublicOutlet() {
  const user = useCurrentUser();

  if (user) {
    return <Navigate to="/game/portal" replace />;
  }

  return <Outlet />;
}
