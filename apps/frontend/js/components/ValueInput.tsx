import * as React from 'react';
import OutlinedInput from '@mui/material/OutlinedInput';
import InputLabel from '@mui/material/InputLabel';
import FormControl from '@mui/material/FormControl';

type ValueInputProps = {
    onChangeHandle: (event: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => void
}

export default function ValueInput({ onChangeHandle }: ValueInputProps) {

    return (
        <FormControl fullWidth variant="outlined">
            <InputLabel htmlFor="outlined-adornment-password">Value</InputLabel>
            <OutlinedInput
                id="id-value-input"
                type="number"
                label="Value"
                onChange={onChangeHandle}
            />
        </FormControl>
    );
}