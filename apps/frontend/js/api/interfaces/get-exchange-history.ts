import CurrencyEnum from "../../enums/currency-enum";

interface IExchangeHistoryDTO {
  id: number;
  currency_from: CurrencyEnum;
  currency_to: CurrencyEnum;
  request_date: Date;
  amount: number | null;
  is_error: boolean;
  result: number | null;
}
export default interface IGetExchangeHistoryResponse {
  exchange_history: IExchangeHistoryDTO[];
}

export class ExchangeHistoryEntity {
  id: number;
  currency_from: CurrencyEnum;
  currency_to: CurrencyEnum;
  request_date: Date;
  amount: number | null;
  is_error: boolean;
  result: number | null;
  constructor(
    id: number,
    currency_from: CurrencyEnum,
    currency_to: CurrencyEnum,
    request_date: Date,
    amount: number | null,
    is_error: boolean,
    result: number | null
  ) {
    this.id = id;
    this.currency_from = currency_from;
    this.currency_to = currency_to;
    this.request_date = request_date;
    this.amount = amount;
    this.is_error = is_error;
    this.result = result;
  }
}
