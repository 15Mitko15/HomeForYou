import { SxProps, Theme } from "@mui/material";

type Styles<T extends string> = Record<T, SxProps<Theme>>;

export function makeStyles<T extends string>(styles: Styles<T>): Styles<T> {
  return styles;
}
