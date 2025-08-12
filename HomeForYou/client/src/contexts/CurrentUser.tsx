import {
  createContext,
  ReactNode,
  useContext,
  useEffect,
  useState,
} from "react";
import { userInfoService } from "../services/userInfo";
import { User } from "../types/user";

const UserContext = createContext<User | null | undefined>(undefined);

interface CurrentUserProviderProps {
  children: ReactNode;
}

// eslint-disable-next-line react-refresh/only-export-components
export function useCurrentUser() {
  const user = useContext(UserContext);

  if (user === undefined) {
    throw new Error("useCurrentUser must be used within a CurrentUserProvider");
  }

  return user;
}

export function CurrentUserProvider({ children }: CurrentUserProviderProps) {
  const [user, setUser] = useState<User | null>(userInfoService.initialUser);

  useEffect(() => {
    userInfoService.setHandler(setUser);

    return () => userInfoService.setHandler(null);
  }, []);

  return <UserContext.Provider value={user}>{children}</UserContext.Provider>;
}
