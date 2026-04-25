import { useState, useEffect } from "react";

interface Props {
  name: string;
  size?: number;
}

export function ReactIcon({ name, size = 18 }: Props) {
  const [IconComponent, setIconComponent] = useState<React.ComponentType<{ size?: number }> | null>(null);

  useEffect(() => {
    const prefix = name.slice(0, 2).toLowerCase();

    const libMap: Record<string, string> = {
      lu: "https://esm.sh/react-icons/lu",
      bs: "https://esm.sh/react-icons/bs",
      fi: "https://esm.sh/react-icons/fi",
      md: "https://esm.sh/react-icons/md",
    };

    const url = libMap[prefix];
    if (!url) return;

    import(/* @vite-ignore */ url).then((mod) => {
      const Icon = mod[name];
      if (Icon) setIconComponent(() => Icon);
    });
  }, [name]);

  if (!IconComponent) return <span style={{ width: size, height: size, display: "inline-block" }} />;

  return <IconComponent size={size} />;
}