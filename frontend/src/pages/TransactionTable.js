//TransactionTable.js

import React, { useState } from "react";
import { useRef, useEffect } from 'react';
import CreateIcon from "@material-ui/icons/Create";
import {
	Box, Button, Snackbar, Table,
	TableBody, TableCell, TableHead, TableRow
} from "@material-ui/core";
import DeleteOutlineIcon from "@material-ui/icons/DeleteOutline";
import AddBoxIcon from "@material-ui/icons/AddBox";
import DoneIcon from "@material-ui/icons/Done";
import ClearIcon from "@material-ui/icons/Clear";
import CancelIcon from '@material-ui/icons/Cancel';
import { makeStyles } from "@material-ui/core/styles";
import Alert from "@material-ui/lab/Alert";
import Dialog from "@material-ui/core/Dialog";
import DialogActions from "@material-ui/core/DialogActions";
import DialogContent from "@material-ui/core/DialogContent";
import DialogContentText from "@material-ui/core/DialogContentText";
import DialogTitle from "@material-ui/core/DialogTitle";

// Creating styles
const useStyles = makeStyles({
	root: {
		"& > *": {
			borderBottom: "unset",
		},
	},
	table: {
		minWidth: 650,
	},
	snackbar: {
		bottom: "104px",
	},
});

function TransactionTable() {
	// Creating style object
	const classes = useStyles();

	// Defining a state named rows
	// which we can update by calling on setRows function
	const [rows, setRows] = useState([
		{id: 1, transDate: "15MAR", desc: "GRAB SLAYY SISTER", amount: 100.00, type: "DEBIT", category: "Transportation", userId: 1},  
	]);

    useEffect(() => {
        const fetchPost = async () => {
           const response = await fetch(
              'http://127.0.0.1:5200/transactions?userId=1'
           );
           const data = await response.json();
           console.log(data);
           setRows(data);
        };
        fetchPost();
     }, []);

    // const [categories, setCategories] = useState(["Food", "Transportation", "Apparel", "Rent", "Income"]);
	const [categories] = useState(["food", "travel", "apparel", "transport", "bills", "medical expenses", "subscriptions", "tax", "others"]);

	// Initial states
	const [open, setOpen] = React.useState(false);
	const [isEdit, setEdit] = React.useState(false);
	const [disable, setDisable] = React.useState(true);
	const [showConfirm, setShowConfirm] = React.useState(false);

	// Function For closing the alert snackbar
	const handleClose = (event, reason) => {
		if (reason === "clickaway") {
			return;
		}
		setOpen(false);
	};

	// Function For adding new row object
	const handleAdd = () => {
		setRows([
			...rows,
			{
				id: rows.length + 1, userId: "1", transDate: "", 
                desc: "", amount: 0, type: "", 
                category: ""
			},
		]);
		setEdit(true);
	};

	// Function to handle edit
	const handleEdit = (i) => {
		// If edit mode is true setEdit will 
		// set it to false and vice versa
		setEdit(!isEdit);
	};

	// Function to handle save
	const handleSave = () => {
		setEdit(!isEdit);
		setRows(rows);
		console.log("saved : ", rows);
		setDisable(true);
		setOpen(true);
	};

	const handleCancel = () => {
		// TODO: Go back to originalRows
		// setRows(originalRows); // You need to manage originalRows state when the edit starts
		setEdit(false);
		setDisable(false);
		setOpen(false);
		// Log cancel action
		console.log("Edit cancelled");
	};
	

	// The handleInputChange handler can be set up to handle
	// many different inputs in the form, listen for changes 
	// to input elements and record their values in state
	const handleInputChange = (e, index) => {
		setDisable(false);
		const { name, value } = e.target;
		const updatedRows = [...rows];
		if (name === "category") {
			// Handle category-specific logic
			if (categories.includes(value)) {
				updatedRows[index][name] = value;
			} else {
				// Handle invalid category case, e.g., set an error or revert to previous value
				console.error("Invalid category selected");
			}
		} else {
			// Handle other inputs generically
			updatedRows[index][name] = value;
		}
		updatedRows[index]["UserConfirmation"] = true;
		setRows(updatedRows);
	};

	// Showing delete confirmation to users
	const handleConfirm = () => {
		setShowConfirm(true);
	};

	// Handle the case of delete confirmation where 
	// user click yes delete a specific row of id:i
	const handleRemoveClick = (i) => {
		const list = [...rows];
		list.splice(i, 1);
		setRows(list);
		setShowConfirm(false);
	};

	// Handle the case of delete confirmation 
	// where user click no 
	const handleNo = () => {
		setShowConfirm(false);
	};

    const [postStatus, setPostStatus] = useState(null);

    const onSubmit = async () => {
        try {
            const response = await fetch('http://127.0.0.1:5200/transactionsConfirm', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(rows), // Send rows as the request body
            });
            const data = await response.json();
            setPostStatus(data); // Update state with response status
            console.log(postStatus);
        } catch (error) {
            console.error('Error while submitting:', error);
        }
    };

    // Step 4: Update handleSubmit to call onSubmit
    const handleSubmit = () => {
        onSubmit(); // Call onSubmit function to send POST request
    };
	
	return (
		<TableBody>
			<Snackbar
				open={open}
				autoHideDuration={2000}
				onClose={handleClose}
				className={classes.snackbar}
			>
				<Alert onClose={handleClose} severity="success">
					Record saved successfully!
				</Alert>
			</Snackbar>
			<Box margin={1}>
				<div style={{ display: "flex", justifyContent: "space-between" }}>
					{isEdit ? (
						<>
							<Button onClick={handleAdd}>
								<AddBoxIcon />
								ADD
							</Button>
							{rows.length > 0 && (
								<>
								<Button disabled={disable} align="right" onClick={handleSave}>
									<DoneIcon />
									{disable ? 'SAVE' : 'SAVE'}
								</Button>
								<Button align="right" onClick={handleCancel}>
									<CancelIcon />
									CANCEL
								</Button>
								</>
							)}
						</>
					) : (
						<>
							<Button onClick={handleAdd}>
								<AddBoxIcon />
								ADD
							</Button>
							<Button align="right" onClick={handleEdit}>
								<CreateIcon />
								EDIT
							</Button>
                            <Button align="right" onClick={handleSubmit}>
								<DoneIcon />
								CONFIRM ALL TRANSACTIONS
							</Button>
						</>
					)}
				</div>
				<TableRow align="center"></TableRow>
				<Table className={classes.table} size="small" aria-label="a dense table">
					<TableHead>
						<TableRow>
							<TableCell>Trans Date</TableCell>
							<TableCell>Transaction Description</TableCell>
							<TableCell>Amount</TableCell>
							<TableCell>Type</TableCell>
							<TableCell>Category</TableCell>
						</TableRow>
					</TableHead>
					<TableBody>
						{rows.map((row, i) => (
							<TableRow key={i}>
								{isEdit ? (
									<>
										<TableCell padding="none">
											<input
												value={row.transDate}
												name="transDate"
												onChange={e => handleInputChange(e, i)}
											/>
										</TableCell>
										<TableCell padding="none">
											<input
												value={row.desc}
												name="desc"
												onChange={e => handleInputChange(e, i)}
											/>
										</TableCell>
										<TableCell padding="none">
											<input
												value={row.amount}
												name="amount"
												onChange={e => handleInputChange(e, i)}
											/>
										</TableCell>
										<TableCell padding="none">
											<input
												value={row.type}
												name="type"
												onChange={e => handleInputChange(e, i)}
											/>
										</TableCell>
										<TableCell padding="none">
											<select
												style={{ width: "100%" }}
												name="category"
												value={row.category}
												onChange={e => handleInputChange(e, i)}
											>
												{categories.map((cat, index) => (
													<option key={index} value={cat}>
														{cat}
													</option>
												))}
											</select>
										</TableCell>
									</>
								) : (
									<>
										<TableCell>{row.transDate}</TableCell>
										<TableCell>{row.desc}</TableCell>
										<TableCell>{row.amount}</TableCell>
										<TableCell>{row.type}</TableCell>
										<TableCell>{row.category}</TableCell>
									</>
								)}
								<Button className="mr10" onClick={handleConfirm}>
									{isEdit ? <ClearIcon /> : <DeleteOutlineIcon />}
								</Button>
							</TableRow>
						))}
					</TableBody>
				</Table>
			</Box>
		</TableBody>
	);
}

export default TransactionTable;
