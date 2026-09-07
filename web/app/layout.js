export const metadata = {
  title: 'Animation Assistant — Teaching Kids to Animate with Kenya\'s Ocean',
  description:
    'An AI-powered animation teaching assistant for kids aged 10–17, built around the 12 Principles of Animation, localized for Kenya\'s Indian Ocean coastline, and aligned to the Kenya CBE curriculum and Raspberry Pi Foundation computing standards.',
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="data:image/svg+xml,<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 100 100'><text y='.9em' font-size='90'>🌊</text></svg>" />
      </head>
      <body>{children}</body>
    </html>
  );
}