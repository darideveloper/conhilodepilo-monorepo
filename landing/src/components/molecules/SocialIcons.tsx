import { FiGlobe, FiInstagram, FiMail } from "react-icons/fi"
import { SiTiktok, SiFacebook } from "react-icons/si"

interface SocialLink {
  icon: string
  url: string
}

const iconMap: Record<string, React.ComponentType<{ size?: number; className?: string }>> = {
  Globe: FiGlobe,
  Instagram: FiInstagram,
  Facebook: SiFacebook,
  TikTok: SiTiktok,
  Mail: FiMail,
}

interface SocialIconsProps {
  links: SocialLink[]
}

export default function SocialIcons({ links }: SocialIconsProps) {
  return (
    <div class="flex gap-4">
      {links.map((link) => {
        const IconComponent = iconMap[link.icon]
        return (
          <a
            key={link.icon}
            class="w-10 h-10 rounded-full bg-white/10 flex items-center justify-center hover:bg-brand-secondary hover:text-ui-bg-dark transition-colors"
            href={link.url}
            target={link.url.startsWith("http") ? "_blank" : undefined}
            rel={link.url.startsWith("http") ? "noopener noreferrer" : undefined}
          >
            {IconComponent ? <IconComponent size={18} /> : null}
          </a>
        )
      })}
    </div>
  )
}
