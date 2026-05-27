import { FiMapPin, FiMessageCircle } from "react-icons/fi"

const iconMap: Record<string, React.ComponentType<{ size?: number; className?: string }>> = {
  MapPin: FiMapPin,
  MessageCircle: FiMessageCircle,
}

interface FooterIconProps {
  name: string
  size?: number
  className?: string
}

export default function FooterIcon({ name, size, className }: FooterIconProps) {
  const IconComponent = iconMap[name]
  return IconComponent ? <IconComponent size={size} className={className} /> : null
}
