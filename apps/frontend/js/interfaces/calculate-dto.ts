import CurrencyEnum from "../enums/currency-enum";


export default interface CalculateDTO {
    currencyFrom: CurrencyEnum,
    currencyTo: CurrencyEnum,
    value: number
}

