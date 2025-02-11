import { createFileRoute } from "@tanstack/react-router";
import clsx from "clsx";
import { Flex, Text, Button, Theme, Box, Card, Avatar, Switch } from "@radix-ui/themes";

export const Route = createFileRoute("/quick-start")({
  component: RouteComponent,
});

function MyApp() {
  return (
    <Flex direction="column" gap="2">
      <Text>Hello from Radix Themes :)</Text>
      <Button>Let's go</Button>
    </Flex>
  );
}

function TestCard() {
  return (
    <Box maxWidth="240px">
      <Card>
        <Flex gap="3" align="center">
          <Avatar
            size="3"
            src="https://images.unsplash.com/photo-1607346256330-dee7af15f7c5?&w=64&h=64&dpr=2&q=70&crop=focalpoint&fp-x=0.67&fp-y=0.5&fp-z=1.4&fit=crop"
            radius="full"
            fallback="T"
          />
          <Box>
            <Text as="div" size="2" weight="bold">
              Teodros Girmay
            </Text>
            <Text as="div" size="2" color="gray">
              Engineering
            </Text>
          </Box>
        </Flex>
      </Card>
      <p className="text-white bg-black w-20">Hello world!</p>
    </Box>
  );
}

const MySwitch = () => {
  return (
    <form>
      <div className={clsx("flex", "items-center")}>
        <label className={clsx("text-base", "pr-3", "select-none")} htmlFor="notification">
          通知を受け取る
        </label>
        <Switch.Root
          className={clsx(
            "group",
            ["w-[42px]", "h-[25px]"],
            ["inline-flex", "flex-shrink-0"],
            ["bg-gradient-to-r", "from-[#EC008C]", "to-[#FC6767]"],
            "relative",
            "cursor-pointer",
            "rounded-full",
            "shadow-md",
            [
              "radix-state-checked:bg-black",
              "radix-state-unchecked:bg-gray-600",
              "radix-state-checked:focus:ring",
              "radix-state-unchecked:focus:ring-1",
            ],
            ["focus:outline-none", "focus:ring-white"],
            ["transition-colors", "duration-200", "ease-in-out"],
            ["border-2", "border-transparent"]
          )}
          id="notification"
        >
          <Switch.Thumb
            className={clsx(
              ["inline-block", "h-[21px]", "w-[21px]"],
              "transform",
              "rounded-full",
              "group-radix-state-checked:translate-x-5",
              "bg-white",
              "shadow-lg",
              "ring-0",
              "pointer-events-none",
              ["transition", "duration-200", "ease-in-out"],
              "group-radix-state-unchecked:translate-x-0"
            )}
          />
        </Switch.Root>
      </div>
    </form>
  );
};

function RouteComponent() {
  return (
    <html lang="ja">
      <body>
        <Theme>
          {/* <MyApp /> */}
          <TestCard />
        </Theme>
      </body>
    </html>
  );
}
