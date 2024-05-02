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

    const [categories, setCategories] = useState(["Food", "Transportation", "Apparel", "Rent", "Income"]);

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

	// The handleInputChange handler can be set up to handle
	// many different inputs in the form, listen for changes 
	// to input elements and record their values in state
	const handleInputChange = (e, index) => {
		setDisable(false);
		const { name, value } = e.target;
		const list = [...rows];
		list[index][name] = value;
        list[index]["UserConfirmation"] = true; //Indicate change in row
		setRows(list);
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
								<Button disabled={disable} align="right" onClick={handleSave}>
									<DoneIcon />
									{disable ? 'SAVE' : 'SAVE'}
								</Button>
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
