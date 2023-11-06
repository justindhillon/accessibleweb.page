import { fileURLToPath } from "url";

export const settings = fileURLToPath(new URL("../public/", import.meta.url));
