import Box from "@mui/material/Box";
import * as React from "react";
import { getExchangeHistory } from "../api/exchange-history";
import { ExchangeHistoryEntity } from "../api/interfaces/get-exchange-history";
import { List, ListItem, Typography, styled } from "@mui/material";
import ArrowCircleRightIcon from "@mui/icons-material/ArrowCircleRight";

const MediaBox = styled(Box)(({ theme }) => ({
  width: "100%",
  height: "calc( 100% - 41px)",
  overflow: "auto",
  [theme.breakpoints.up("sm")]: {
    height: "400px",
  },
}));

function CurrencyText({ children }:React.PropsWithChildren) {
  return <Typography component={"span"} fontWeight={"bold"}>{children}</Typography>;
}

export default function HistoryContainer() {
  const [history, setHistory] = React.useState<
    ExchangeHistoryEntity[] | undefined
  >(undefined);

  React.useEffect(() => {
    (async () => {
      const history = await getExchangeHistory();
      setHistory(history);
    })();
  }, []);
  return (
    <MediaBox>
      <List aria-label="exchange history">
        {history?.map((item) => {
          return (
            <ListItem key={item.id}>
              <Typography>
                {item.amount}{" "}
                <CurrencyText>
                  {item.currency_from.toUpperCase()}
                </CurrencyText>
              </Typography>
              <ArrowCircleRightIcon
                fontSize="small"
                color="primary"
                sx={{ paddingLeft: "10px", paddingRight: "10px" }}
              />
              <Typography>
                {item.result}{" "}
                <CurrencyText>
                  {item.currency_to.toUpperCase()}
                </CurrencyText>
              </Typography>
            </ListItem>
          );
        })}
      </List>
    </MediaBox>
  );
}
