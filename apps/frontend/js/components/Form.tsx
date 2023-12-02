import * as React from 'react'
import InputLabel from '@mui/material/InputLabel'
import FormControl from '@mui/material/FormControl'
import CurrencyEnum from '../enums/currency-enum'
import Select, { SelectChangeEvent } from '@mui/material/Select'
import MenuItem from '@mui/material/MenuItem'
import Grid from '@mui/material/Grid'
import Button from '@mui/material/Button'
import ValueInput from './ValueInput'

export default function Form() {
    const keys = Object.keys(CurrencyEnum)
    const [from, setFrom] = React.useState(null);
    const [to, setTo] = React.useState(null);
    const [value, setValue] = React.useState('');


    const handleFromChange = (event: SelectChangeEvent) => {
        setFrom(event.target.value);
    }
    const handleToChange = (event: SelectChangeEvent) => {
        setTo(event.target.value);
    }
    const handleValueChange = (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
        setValue(event.target.value);
    }

    const onSubmitHandle = (e: React.FormEvent) => {
        e.preventDefault();
    }
    return (
        <Grid container justifyContent={'center'} alignItems={'center'} height={"100%"}>
            <Grid item width={300} height={300} >
                <form onSubmit={onSubmitHandle}>
                    <Grid container justifyContent={'center'} alignItems={'center'} spacing={1}>
                        <Grid item width={"100%"}>
                            <FormControl fullWidth>
                                <InputLabel id="id-input-label-from">From</InputLabel>
                                <Select
                                    labelId="id-label-from"
                                    id="id-from"
                                    value={from}
                                    label="From"
                                    onChange={handleFromChange}
                                >
                                    {keys.map((key: string) => {
                                        return <MenuItem key={key.toLowerCase()} value={key.toLowerCase()}>{key}</MenuItem>
                                    })}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item width={"100%"}>
                            <FormControl fullWidth>
                                <InputLabel id="id-input-label-to">From</InputLabel>
                                <Select
                                    labelId="id-label-to"
                                    id="id-to"
                                    value={to}
                                    label="To"
                                    onChange={handleToChange}
                                >
                                    {keys.map((key: string) => {
                                        return <MenuItem value={key.toLowerCase()}>{key}</MenuItem>
                                    })}
                                </Select>
                            </FormControl>
                        </Grid>
                        <Grid item width={"100%"}>
                            <ValueInput onChangeHandle={handleValueChange}></ValueInput>
                        </Grid>
                        <Grid item width={"100%"}>
                            <Button fullWidth variant='contained' type='submit'>
                                Calculate
                            </Button>
                        </Grid>
                    </Grid>
                </form>
            </Grid>
        </Grid>
    );
}