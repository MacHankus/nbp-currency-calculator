import urls from "./urls";
import axios from "axios";
import { ApiError, ApiWrongResponse } from "./exceptions";
import IGetExchangeHistoryResponse, {
  ExchangeHistoryEntity,
} from "./interfaces/get-exchange-history";

export async function getExchangeHistory(): Promise<ExchangeHistoryEntity[]> {
  try {
    const response = await axios.get<IGetExchangeHistoryResponse>(
      urls.EXCHANGE_HISTORY
    );
    if (response.status != 200) {
      throw new ApiWrongResponse(
        "Wrong response",
        "Status code: " + response.status.toString()
      );
    }

    return response.data.exchange_history.map<ExchangeHistoryEntity>((item) => {
        return new ExchangeHistoryEntity(
        item.id,
        item.currency_from,
        item.currency_to,
        item.request_date,
        item.amount,
        item.is_error,
        item.result
        );
    });

  } catch (err) {
    console.log(err);
    throw new ApiError("Api Error", "");
  }
}
