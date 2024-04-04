import * as React from 'react'
import InputLabel from '@mui/material/InputLabel'
import FormControl from '@mui/material/FormControl'
import CurrencyEnum from '../enums/currency-enum'
import Select, { type SelectChangeEvent } from '@mui/material/Select'
import MenuItem from '@mui/material/MenuItem'
import Grid from '@mui/material/Grid'
import Button from '@mui/material/Button'
import ValueInput from './ValueInput'
import { postCalculate } from '../api/calculate'
import type CalculateDTO from '../interfaces/calculate-dto'
import TextField from '@mui/material/TextField'
import { ZodError, z } from 'zod'
import { Typography } from '@mui/material'
import History from './History'

export default function Form() {
    const keys = Object.keys(CurrencyEnum)
    const [from, setFrom] = React.useState<CurrencyEnum>(CurrencyEnum.EUR)
    const [to, setTo] = React.useState<CurrencyEnum>(CurrencyEnum.EUR)
    const [value, setValue] = React.useState<number>(0)
    const [valueError, setValueError] = React.useState('')
    const [requestError, setRequestError] = React.useState('')
    const [result, setResult] = React.useState<number | undefined>(undefined)

    const VALUE_ERROR = "Value should be positive number."

    const handleFromChange = (event: SelectChangeEvent) => {
        setFrom(event.target.value as CurrencyEnum)
    }
    const handleToChange = (event: SelectChangeEvent) => {
        setTo(event.target.value as CurrencyEnum)
    }
    const handleValueChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setValue(Number(event.target.value))
    }

    const onSubmitHandle = async (e: React.FormEvent) => {
        e.preventDefault()
        setRequestError('')
        let number = null
        const positiveNumberValidation = z.number().positive()
        try{
            number = positiveNumberValidation.parse(value)
        }catch(error){
            if (error instanceof ZodError){
                setValueError(VALUE_ERROR)
                return
            }
        }
        if (!number){
            return
        }
        const dto: CalculateDTO = {
            currencyFrom: from,
            currencyTo: to,
            value: number
        }
    const calculate = await postCalculate(dto)
    const returned = calculate.value
    try{
        const returnedNumber = Number(returned)
        if (!returnedNumber){
            throw new Error()
        }
        positiveNumberValidation.parse(returnedNumber)
    } catch(error){
        setRequestError('Something wrong with the result. Try again later.')
        return
    }
    setResult(calculate.value)
        setValueError('')
    }

    return (
        <Grid container justifyContent={'center'} alignItems={'center'} height={'100%'}>
            <Grid item width={300} height={300} >
                <form onSubmit={onSubmitHandle}>
                    <Grid container justifyContent={'center'} alignItems={'center'} spacing={2}>
                        <Grid item width={'100%'} key="grid-from">
                            <FormControl fullWidth>
                                <InputLabel id="id-input-label-from">From</InputLabel>
                                <Select
                                    labelId="id-label-from"
                                    id="id-from"
                                    value={from || ''}
                                    label="From"
                                    onChange={handleFromChange}
                                >
                                    {keys.map((key: string) => {
                                        return <MenuItem key={key.toLowerCase()} value={key.toLowerCase()}>{key}</MenuItem>
                                    })}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item width={'100%'} key="grid-to">
                            <FormControl fullWidth>
                                <InputLabel id="id-input-label-to">To</InputLabel>
                                <Select
                                    labelId="id-label-to"
                                    id="id-to"
                                    value={to || ''}
                                    label="To"
                                    onChange={handleToChange}
                                >
                                    {keys.map((key: string) => {
                                        return <MenuItem key={key} value={key.toLowerCase()}>{key}</MenuItem>
                                    })}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item width={'100%'} key="grid-input">
                            <ValueInput error={valueError === '' ? false : true} helperText={valueError === '' ? '' : valueError} onChangeHandle={handleValueChange} type={'number'} value={value}></ValueInput>
                        </Grid>
                        <Grid item width={'100%'} key="grid-submit">
                            <Button fullWidth variant='contained' type='submit'>
                                Calculate
                            </Button>
                            <Typography color={'red'}>
                                {requestError === '' ? '' : requestError }
                            </Typography>
                        </Grid>
                        <Grid item width={'100%'} key="grid-result">
                            <FormControl fullWidth>
                                <TextField
                                    id="id-result"
                                    defaultValue={result ? result.toString() : 'Waiting...'}
                                    value={result ? result.toString() : 'Waiting...'}
                                    label="Result"
                                    InputProps={{
                                        readOnly: true,
                                      }}
                                >
                                    
                                </TextField >
                            </FormControl>
                        </Grid>
                        <Grid item width={'100%'} key="grid-history">
                            <History/>
                        </Grid>
                    </Grid>
                </form>
            </Grid>
        </Grid>
    )
}
