{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Import Libraries"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "%matplotlib inline\n",
    "import pickle"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Get the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data = pd.read_csv('Datasets/asd_dataset.csv',index_col=0)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data PreProcessing"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A1</th>\n",
       "      <th>A2</th>\n",
       "      <th>A3</th>\n",
       "      <th>A4</th>\n",
       "      <th>A5</th>\n",
       "      <th>A6</th>\n",
       "      <th>A7</th>\n",
       "      <th>A8</th>\n",
       "      <th>A9</th>\n",
       "      <th>A10</th>\n",
       "      <th>Age_Mons</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Jaundice</th>\n",
       "      <th>Family_mem_with_ASD</th>\n",
       "      <th>Who_completed_the_test</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Case_No</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>28</td>\n",
       "      <td>f</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>24</td>\n",
       "      <td>m</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>f</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>21</td>\n",
       "      <td>m</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>33</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>33</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>m</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>22</td>\n",
       "      <td>m</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>Health Care Professional</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  Age_Mons Sex Jaundice  \\\n",
       "Case_No                                                                   \n",
       "1         0   0   0   0   0   0   1   1   0    1        28   f      yes   \n",
       "2         1   1   0   0   0   1   1   0   0    0        36   m      yes   \n",
       "3         1   0   0   0   0   0   1   1   0    1        36   m      yes   \n",
       "4         1   1   1   1   1   1   1   1   1    1        24   m       no   \n",
       "5         1   1   0   1   1   1   1   1   1    1        20   f       no   \n",
       "6         1   1   0   0   1   1   1   1   1    1        21   m       no   \n",
       "7         1   0   0   1   1   1   0   0   1    0        33   m      yes   \n",
       "8         0   1   0   0   1   0   1   1   1    1        33   m      yes   \n",
       "9         0   0   0   0   0   0   1   0   0    1        36   m       no   \n",
       "10        1   1   1   0   1   1   0   1   1    1        22   m       no   \n",
       "\n",
       "        Family_mem_with_ASD    Who_completed_the_test Class  \n",
       "Case_No                                                      \n",
       "1                        no             family member    No  \n",
       "2                        no             family member   Yes  \n",
       "3                        no             family member   Yes  \n",
       "4                        no             family member   Yes  \n",
       "5                       yes             family member   Yes  \n",
       "6                        no             family member   Yes  \n",
       "7                        no             family member   Yes  \n",
       "8                        no             family member   Yes  \n",
       "9                        no             family member    No  \n",
       "10                       no  Health Care Professional   Yes  "
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A1</th>\n",
       "      <th>A2</th>\n",
       "      <th>A3</th>\n",
       "      <th>A4</th>\n",
       "      <th>A5</th>\n",
       "      <th>A6</th>\n",
       "      <th>A7</th>\n",
       "      <th>A8</th>\n",
       "      <th>A9</th>\n",
       "      <th>A10</th>\n",
       "      <th>Age_Mons</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Jaundice</th>\n",
       "      <th>Family_mem_with_ASD</th>\n",
       "      <th>Who_completed_the_test</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Case_No</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1050</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>24</td>\n",
       "      <td>f</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>family member</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1051</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>12</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1052</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>18</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1053</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>19</td>\n",
       "      <td>m</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>family member</td>\n",
       "      <td>No</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>1054</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>24</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>yes</td>\n",
       "      <td>family member</td>\n",
       "      <td>Yes</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  Age_Mons Sex Jaundice  \\\n",
       "Case_No                                                                   \n",
       "1050      0   0   0   0   0   0   0   0   0    1        24   f       no   \n",
       "1051      0   0   1   1   1   0   1   0   1    0        12   m      yes   \n",
       "1052      1   0   1   1   1   1   1   1   1    1        18   m      yes   \n",
       "1053      1   0   0   0   0   0   0   1   0    1        19   m       no   \n",
       "1054      1   1   0   0   1   1   0   1   1    0        24   m      yes   \n",
       "\n",
       "        Family_mem_with_ASD Who_completed_the_test Class  \n",
       "Case_No                                                   \n",
       "1050                    yes          family member    No  \n",
       "1051                     no          family member   Yes  \n",
       "1052                     no          family member   Yes  \n",
       "1053                    yes          family member    No  \n",
       "1054                    yes          family member   Yes  "
      ]
     },
     "execution_count": 4,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.tail()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Age_Mons',\n",
       "       'Sex', 'Jaundice', 'Family_mem_with_ASD', 'Who_completed_the_test',\n",
       "       'Class'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['No', 'Yes'], dtype=object)"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.Class .unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data['Class'].replace('No',0,inplace=True)\n",
    "asd_data['Class'].replace('Yes',1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A1</th>\n",
       "      <th>A2</th>\n",
       "      <th>A3</th>\n",
       "      <th>A4</th>\n",
       "      <th>A5</th>\n",
       "      <th>A6</th>\n",
       "      <th>A7</th>\n",
       "      <th>A8</th>\n",
       "      <th>A9</th>\n",
       "      <th>A10</th>\n",
       "      <th>Age_Mons</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Jaundice</th>\n",
       "      <th>Family_mem_with_ASD</th>\n",
       "      <th>Who_completed_the_test</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Case_No</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>28</td>\n",
       "      <td>f</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>m</td>\n",
       "      <td>yes</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>24</td>\n",
       "      <td>m</td>\n",
       "      <td>no</td>\n",
       "      <td>no</td>\n",
       "      <td>family member</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>f</td>\n",
       "      <td>no</td>\n",
       "      <td>yes</td>\n",
       "      <td>family member</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  Age_Mons Sex Jaundice  \\\n",
       "Case_No                                                                   \n",
       "1         0   0   0   0   0   0   1   1   0    1        28   f      yes   \n",
       "2         1   1   0   0   0   1   1   0   0    0        36   m      yes   \n",
       "3         1   0   0   0   0   0   1   1   0    1        36   m      yes   \n",
       "4         1   1   1   1   1   1   1   1   1    1        24   m       no   \n",
       "5         1   1   0   1   1   1   1   1   1    1        20   f       no   \n",
       "\n",
       "        Family_mem_with_ASD Who_completed_the_test  Class  \n",
       "Case_No                                                    \n",
       "1                        no          family member      0  \n",
       "2                        no          family member      1  \n",
       "3                        no          family member      1  \n",
       "4                        no          family member      1  \n",
       "5                       yes          family member      1  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['f', 'm'], dtype=object)"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.Sex.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data['Sex'].replace('m',0,inplace=True)\n",
    "asd_data['Sex'].replace('f',1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['yes', 'no'], dtype=object)"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.Jaundice.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data['Jaundice'].replace('no',0,inplace=True)\n",
    "asd_data['Jaundice'].replace('yes',1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['no', 'yes'], dtype=object)"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.Family_mem_with_ASD.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data['Family_mem_with_ASD'].replace('no',0,inplace=True)\n",
    "asd_data['Family_mem_with_ASD'].replace('yes',1,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['family member', 'Health Care Professional',\n",
       "       'Health care professional', 'Self', 'Others'], dtype=object)"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.Who_completed_the_test.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data['Who_completed_the_test'].replace('Health Care Professional','Health care professional',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "array(['family member', 'Health care professional', 'Self', 'Others'],\n",
       "      dtype=object)"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.Who_completed_the_test.unique()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data['Who_completed_the_test'].replace('family member',0,inplace=True)\n",
    "asd_data['Who_completed_the_test'].replace('Health care professional',1,inplace=True)\n",
    "asd_data['Who_completed_the_test'].replace('Self',2,inplace=True)\n",
    "asd_data['Who_completed_the_test'].replace('Others',3,inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A1</th>\n",
       "      <th>A2</th>\n",
       "      <th>A3</th>\n",
       "      <th>A4</th>\n",
       "      <th>A5</th>\n",
       "      <th>A6</th>\n",
       "      <th>A7</th>\n",
       "      <th>A8</th>\n",
       "      <th>A9</th>\n",
       "      <th>A10</th>\n",
       "      <th>Age_Mons</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Jaundice</th>\n",
       "      <th>Family_mem_with_ASD</th>\n",
       "      <th>Who_completed_the_test</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Case_No</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>28</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>2</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>3</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>4</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>5</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>6</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>7</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>33</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>8</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>33</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>9</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>10</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>22</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  Age_Mons  Sex  Jaundice  \\\n",
       "Case_No                                                                     \n",
       "1         0   0   0   0   0   0   1   1   0    1        28    1         1   \n",
       "2         1   1   0   0   0   1   1   0   0    0        36    0         1   \n",
       "3         1   0   0   0   0   0   1   1   0    1        36    0         1   \n",
       "4         1   1   1   1   1   1   1   1   1    1        24    0         0   \n",
       "5         1   1   0   1   1   1   1   1   1    1        20    1         0   \n",
       "6         1   1   0   0   1   1   1   1   1    1        21    0         0   \n",
       "7         1   0   0   1   1   1   0   0   1    0        33    0         1   \n",
       "8         0   1   0   0   1   0   1   1   1    1        33    0         1   \n",
       "9         0   0   0   0   0   0   1   0   0    1        36    0         0   \n",
       "10        1   1   1   0   1   1   0   1   1    1        22    0         0   \n",
       "\n",
       "         Family_mem_with_ASD  Who_completed_the_test  Class  \n",
       "Case_No                                                      \n",
       "1                          0                       0      0  \n",
       "2                          0                       0      1  \n",
       "3                          0                       0      1  \n",
       "4                          0                       0      1  \n",
       "5                          1                       0      1  \n",
       "6                          0                       0      1  \n",
       "7                          0                       0      1  \n",
       "8                          0                       0      1  \n",
       "9                          0                       0      0  \n",
       "10                         0                       1      1  "
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A1</th>\n",
       "      <th>A2</th>\n",
       "      <th>A3</th>\n",
       "      <th>A4</th>\n",
       "      <th>A5</th>\n",
       "      <th>A6</th>\n",
       "      <th>A7</th>\n",
       "      <th>A8</th>\n",
       "      <th>A9</th>\n",
       "      <th>A10</th>\n",
       "      <th>Age_Mons</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Jaundice</th>\n",
       "      <th>Family_mem_with_ASD</th>\n",
       "      <th>Who_completed_the_test</th>\n",
       "      <th>Class</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>count</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "      <td>1054.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>mean</td>\n",
       "      <td>0.563567</td>\n",
       "      <td>0.448767</td>\n",
       "      <td>0.401328</td>\n",
       "      <td>0.512334</td>\n",
       "      <td>0.524668</td>\n",
       "      <td>0.576850</td>\n",
       "      <td>0.649905</td>\n",
       "      <td>0.459203</td>\n",
       "      <td>0.489564</td>\n",
       "      <td>0.586338</td>\n",
       "      <td>27.867173</td>\n",
       "      <td>0.302657</td>\n",
       "      <td>0.273245</td>\n",
       "      <td>0.161290</td>\n",
       "      <td>0.043643</td>\n",
       "      <td>0.690702</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>std</td>\n",
       "      <td>0.496178</td>\n",
       "      <td>0.497604</td>\n",
       "      <td>0.490400</td>\n",
       "      <td>0.500085</td>\n",
       "      <td>0.499628</td>\n",
       "      <td>0.494293</td>\n",
       "      <td>0.477226</td>\n",
       "      <td>0.498569</td>\n",
       "      <td>0.500128</td>\n",
       "      <td>0.492723</td>\n",
       "      <td>7.980354</td>\n",
       "      <td>0.459626</td>\n",
       "      <td>0.445837</td>\n",
       "      <td>0.367973</td>\n",
       "      <td>0.257817</td>\n",
       "      <td>0.462424</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>min</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>12.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>25%</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>23.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>50%</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>30.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>75%</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>max</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>36.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>3.000000</td>\n",
       "      <td>1.000000</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "                A1           A2           A3           A4           A5  \\\n",
       "count  1054.000000  1054.000000  1054.000000  1054.000000  1054.000000   \n",
       "mean      0.563567     0.448767     0.401328     0.512334     0.524668   \n",
       "std       0.496178     0.497604     0.490400     0.500085     0.499628   \n",
       "min       0.000000     0.000000     0.000000     0.000000     0.000000   \n",
       "25%       0.000000     0.000000     0.000000     0.000000     0.000000   \n",
       "50%       1.000000     0.000000     0.000000     1.000000     1.000000   \n",
       "75%       1.000000     1.000000     1.000000     1.000000     1.000000   \n",
       "max       1.000000     1.000000     1.000000     1.000000     1.000000   \n",
       "\n",
       "                A6           A7           A8           A9          A10  \\\n",
       "count  1054.000000  1054.000000  1054.000000  1054.000000  1054.000000   \n",
       "mean      0.576850     0.649905     0.459203     0.489564     0.586338   \n",
       "std       0.494293     0.477226     0.498569     0.500128     0.492723   \n",
       "min       0.000000     0.000000     0.000000     0.000000     0.000000   \n",
       "25%       0.000000     0.000000     0.000000     0.000000     0.000000   \n",
       "50%       1.000000     1.000000     0.000000     0.000000     1.000000   \n",
       "75%       1.000000     1.000000     1.000000     1.000000     1.000000   \n",
       "max       1.000000     1.000000     1.000000     1.000000     1.000000   \n",
       "\n",
       "          Age_Mons          Sex     Jaundice  Family_mem_with_ASD  \\\n",
       "count  1054.000000  1054.000000  1054.000000          1054.000000   \n",
       "mean     27.867173     0.302657     0.273245             0.161290   \n",
       "std       7.980354     0.459626     0.445837             0.367973   \n",
       "min      12.000000     0.000000     0.000000             0.000000   \n",
       "25%      23.000000     0.000000     0.000000             0.000000   \n",
       "50%      30.000000     0.000000     0.000000             0.000000   \n",
       "75%      36.000000     1.000000     1.000000             0.000000   \n",
       "max      36.000000     1.000000     1.000000             1.000000   \n",
       "\n",
       "       Who_completed_the_test        Class  \n",
       "count             1054.000000  1054.000000  \n",
       "mean                 0.043643     0.690702  \n",
       "std                  0.257817     0.462424  \n",
       "min                  0.000000     0.000000  \n",
       "25%                  0.000000     0.000000  \n",
       "50%                  0.000000     1.000000  \n",
       "75%                  0.000000     1.000000  \n",
       "max                  3.000000     1.000000  "
      ]
     },
     "execution_count": 20,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "data = asd_data.groupby('Class')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [],
   "source": [
    "df=data.describe()\n",
    "#data.describe().transpose()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[3.579e+02 2.878e+02 2.122e+02 3.605e+02 4.889e+02 5.048e+02 4.886e+02\n",
      " 2.348e+02 5.260e+02 3.516e+01 4.720e+00 1.477e+01 5.802e+00 1.918e-01\n",
      " 6.959e-01]\n",
      "[[0 0 1 0]\n",
      " [0 1 1 0]\n",
      " [0 0 1 0]\n",
      " [1 1 1 1]\n",
      " [1 1 1 1]]\n"
     ]
    }
   ],
   "source": [
    "from numpy import set_printoptions\n",
    "from sklearn.feature_selection import SelectKBest\n",
    "from sklearn.feature_selection import f_classif\n",
    "\n",
    "X = asd_data.drop(['Class'], axis=1)\n",
    "y = asd_data['Class']\n",
    "# feature extraction\n",
    "test = SelectKBest(score_func=f_classif, k=4)\n",
    "fit = test.fit(X, y)\n",
    "# summarize scores\n",
    "set_printoptions(precision=3)\n",
    "print(fit.scores_)\n",
    "features = fit.transform(X)\n",
    "# summarize selected features\n",
    "print(features[0:5,:])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Index(['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Age_Mons',\n",
       "       'Sex', 'Jaundice', 'Family_mem_with_ASD', 'Who_completed_the_test',\n",
       "       'Class'],\n",
       "      dtype='object')"
      ]
     },
     "execution_count": 24,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "asd_data.columns"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [],
   "source": [
    "name = ['A1', 'A2', 'A3', 'A4', 'A5', 'A6', 'A7', 'A8', 'A9', 'A10', 'Age_Mons',\n",
    "       'Sex', 'Jaundice', 'Family_mem_with_ASD', 'Who_completed_the_test']\n",
    "importance = fit.scores_"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x18fab90ee88>"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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AQEAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAAAAAAGuIqAAAAAAAAAACAhrgKAAAAAAAAAACgIa4CAAAAAAAAAABoiKsAAAAAAAAAAAAa4ioAAAAAAAAAAICGuAoAAAAAAAAAAKAhrgIAAAAAAAAAAGiIqwAAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAAAAAAGuIqAAAAAAAAAACAhrgKAAAAAAAAAACgIa4CAAAAAAAAAABoiKsAAAAAAAAAAAAa4ioAAAAAAAAAAICGuAoAAAAAAAAAAKAhrgIAAAAAAAAAAGiIqwAAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAAAAAAGuIqAAAAAAAAAACAhrgKAAAAAAAAAACgIa4CAAAAAAAAAABoiKsAAAAAAAAAAAAa4ioAAAAAAAAAAICGuAoAAAAAAAAAAKAhrgIAAAAAAAAAAGiIqwAAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAAAAAAGuIqAAAAAAAAAACAhrgKAAAAAAAAAACgIa4CAAAAAAAAAABoiKsAAAAAAAAAAAAa4ioAAAAAAAAAAICGuAoAAAAAAAAAAKAhrgIAAAAAAAAAAGiIqwAAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAAAAAAGuIqAAAAAAAAAACAhrgKAAAAAAAAAACgIa4CAAAAAAAAAABoiKsAAAAAAAAAAAAa4ioAAAAAAAAAAICGuAoAAAAAAAAAAKAhrgIAAAAAAAAAAGiIqwAAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAAAAAAGuIqAAAAAAAAAACAhrgKAAAAAAAAAACgIa4CAAAAAAAAAABoiKsAAAAAAAAAAAAa4ioAAAAAAAAAAICGuAoAAAAAAAAAAKAhrgIAAAAAAAAAAGiIqwAAAAAAAAAAABriKgAAAAAAAAAAgIa4CgAAAAAAAAAAoCGuAgAAAAAAAAAAaIirAAAAAAAA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\n",
      "text/plain": [
       "<Figure size 3000x700 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(30,7), dpi=100)\n",
    "sns.barplot(x=name, y=importance)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [],
   "source": [
    "df.to_excel('new.xlsx')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [],
   "source": [
    "asd_data.to_excel('Datasets\\cleandata.xlsx')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Data Analysis"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x18faaea2ec8>"
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAAJPCAYAAACwzFkOAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzde7TdZX3n8c+3IUQuCQExBBdgYQTlotVFSgWk6oxSGMp4XQuminYqtArocKk6iIyoZbRekEGFVmqLi1VHbKuOonJRSu1wUUFUUGxBKREhiYACckkwfeaPs084nFxMnpyTfU7O67XWbx3283t+ez+/f1hZ7/Xs/avWWgAAAACADfMbw14AAAAAAExHwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADpsMewFTAVVVUmemuTBYa8FAAAAgKGbm+Su1lpb1yRhbcRTk9w57EUAAAAAMGXskuSn65ogrI14MEl+8pOfZN68ecNeCwAAAABD8sADD2TXXXdN1uObjcLaGPPmzRPWAAAAAFgvHl4AAAAAAB2ENQAAAADoIKwBAAAAQAe/sQYAAADAE6xcuTKPPfbYsJcxKWbPnp1Zs2ZNyHsJawAAAAAkSVprWbJkSX7xi18MeymTav78+Vm4cGGqaqPeR1gDAAAAIElWRbUFCxZk66233ujwNNW01vLwww9n2bJlSZKdd955o95PWAMAAAAgK1euXBXVnvzkJw97OZNmq622SpIsW7YsCxYs2KivhXp4AQAAAACrflNt6623HvJKJt/oPW7s78gJawAAAACssrl9/XNNJuoehTUAAAAA6CCsAQAAAEAHYQ0AAACASVVV+fznPz/sZUw4YQ0AAACAjbJkyZK86U1vyh577JE5c+Zk1113zZFHHpmvfe1rw17apNpi2AsAAAAAYPr6t3/7txx88MGZP39+3v/+9+fZz352HnvssVx22WU54YQT8sMf/nDYS5w0dqwBAAAA0O34449PVeWb3/xmXvWqV2WvvfbKvvvum1NOOSXXXXfdGq9529velr322itbb7119thjj5xxxhl57LHHVp3/7ne/mxe96EWZO3du5s2bl/333z/XX399kuSOO+7IkUceme233z7bbLNN9t1333z5y1/eJPc6nh1rAAAAAHS57777cumll+ass87KNttss9r5+fPnr/G6uXPn5sILL8xTn/rU3HTTTTnuuOMyd+7cvPWtb02SvPrVr85zn/vcnH/++Zk1a1a+853vZPbs2UmSE044IStWrMjXv/71bLPNNvnBD36QbbfddvJuch2ENQAAAAC63HbbbWmt5ZnPfOYGXfeOd7xj1X//5m/+Zk499dRcfPHFq8La4sWL85a3vGXV++65556r5i9evDivfOUr86xnPStJsscee2zsbXTzVVAAAAAAurTWkow89XND/P3f/32e//znZ+HChdl2221zxhlnZPHixavOn3LKKTn22GPz4he/OO973/vyox/9aNW5N7/5zfmzP/uzHHzwwXnnO9+Z733vexNzMx2ENQAAAAC67Lnnnqmq3HLLLet9zXXXXZejjz46hx9+eC655JLceOONOf3007NixYpVc84888x8//vfzxFHHJErr7wy++yzTz73uc8lSY499tj8+Mc/zjHHHJObbropixYtykc+8pEJv7f1IawBAAAA0GWHHXbI7/3e7+VjH/tYHnroodXO/+IXv1ht7Oqrr87Tnva0nH766Vm0aFH23HPP3HHHHavN22uvvXLyySfn8ssvzyte8Yr8zd/8zapzu+66a97whjfks5/9bE499dRccMEFE3tj60lYAwAAAKDbeeedl5UrV+aAAw7IP/zDP+TWW2/NLbfcknPPPTcHHnjgavOf/vSnZ/Hixfn0pz+dH/3oRzn33HNX7UZLkkceeSQnnnhirrrqqtxxxx25+uqr861vfSt77713kuSkk07KZZddlttvvz3f/va3c+WVV646t6l5eAEAAAAA3Xbfffd8+9vfzllnnZVTTz01d999d57ylKdk//33z/nnn7/a/Je+9KU5+eSTc+KJJ2b58uU54ogjcsYZZ+TMM89MksyaNSv33ntvXvva12bp0qXZcccd84pXvCLvete7kiQrV67MCSeckDvvvDPz5s3LYYcdlg9/+MOb8pZXqdEfmZvJqmpekvvvv//+zJs3b9jLAWaow864eNhLANbh0vccNewlAABMqkcffTS33357dt999zzpSU8a9nIm1bru9YEHHsh2222XJNu11h5Y1/v4KigAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAA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\n",
      "text/plain": [
       "<Figure size 1500x700 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,7), dpi=100)\n",
    "sns.countplot(x='Sex',hue='Class',data=asd_data, palette='Set1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x18fabf7f3c8>"
      ]
     },
     "execution_count": 30,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABNYAAAKbCAYAAAA5Ywc3AAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzde7SddX3v+8/X3JCQENzKbYg0bINF8FYiW7yzt1I4bLcWewaOemsrnlrAHi5HPRQpWOrGoiIbFcaW0xZ3R7vFehvqlluLlLNFqoAgWnuKGhPZJISLBQRMEH/njzVXOl0kIfllrcx1eb3GmGNlPs9vPvnOf9/jN5+nWmsBAAAAALbPk0Y9AAAAAADMRMIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0GH+qAeYDqqqkuyb5MFRzwIAAADAyC1JcmdrrW1tkbA2Zt8kd4x6CAAAAACmjacn+V9bWyCsjXkwSX784x9n6dKlo54FAAAAgBF54IEHst9++yXb8MtGYW3I0qVLhTUAAAAAtomHFwAAAABAB2ENAAAAADoIawAAAADQwT3WtlFrLT//+c/z2GOPjXqUKTFv3rzMnz8/VTXqUQAAAABmBGFtG2zcuDFr167Nww8/POpRptSuu+6affbZJwsXLhz1KAAAAADTnrD2BH7xi19k1apVmTdvXvbdd98sXLhw1u3qaq1l48aNufvuu7Nq1aqsWLEiT3qSXwkDAAAAbI2w9gQ2btyYX/ziF9lvv/2y6667jnqcKfPkJz85CxYsyOrVq7Nx48bssssuox4JAAAAYFqzLWkbzYUdXHPhOwIAAABMFiUFAAAAADoIayNUVfnCF74w6jEAAAAA6CCsTaF169blne98Zw444IAsWrQo++23X17zmtfk7/7u70Y9GgAAAAA7yMMLpsiPfvSjvOQlL8myZcty3nnn5bnPfW4effTRXHnllTnxxBPzT//0T6MeEQAAAIAdYMfaFDnhhBNSVfnGN76R3/zN38yBBx6Ygw8+OKeeempuuOGGzX7mPe95Tw488MDsuuuuOeCAA3LmmWfm0Ucf3XT+1ltvzRFHHJElS5Zk6dKlOfTQQ3PjjTcmSVavXp3XvOY12WOPPbJ48eIcfPDB+cpXvrJTvisAAADAXGTH2hS47777csUVV+T9739/Fi9e/Ljzy5Yt2+znlixZkksvvTT77rtvbrvttrz97W/PkiVL8u53vztJ8sY3vjEveMELcvHFF2fevHm55ZZbsmDBgiTJiSeemI0bN+a6667L4sWL84//+I/Zbbfdpu5LAgAAAMxxwtoU+P73v5/WWn71V391uz733ve+d9O/f+VXfiWnnXZaLrvssk1hbc2aNXnXu9616borVqzYtH7NmjV5/etfn+c85zlJkgMOOGBHvwYAAAAAW+GnoFOgtZZk7Kmf2+Mzn/lMXvrSl2bvvffObrvtljPPPDNr1qzZdP7UU0/N8ccfn1e96lX5wAc+kB/84Aebzv3BH/xB/uRP/iQveclLctZZZ+Xb3/725HwZAAAAADZLWJsCK1asSFXle9/73jZ/5oYbbsgb3vCGHH300fnyl7+cb33rWznjjDOycePGTWvOPvvsfPe7380xxxyTa665Js9+9rPz+c9/Pkly/PHH54c//GHe/OY357bbbsvKlSvz0Y9+dNK/GwAAAABjhLUp8JSnPCW//uu/no9//ON56KGHHnf+X/7lXx537Gtf+1r233//nHHGGVm5cmVWrFiR1atXP27dgQcemFNOOSVXXXVVjj322PzFX/zFpnP77bdf3vGOd+Rzn/tcTjvttFxyySWT+8UAAAAA2ERYmyIXXXRRHnvssRx22GH57Gc/m9tvvz3f+973cuGFF+bwww9/3PpnPvOZWbNmTT71qU/lBz/4QS688MJNu9GS5JFHHslJJ52Ua6+9NqtXr87Xvva1fPOb38xBBx2UJDn55JNz5ZVXZtWqVbn55ptzzTXXbDoHAAAAwOTz8IIpsnz58tx88815//vfn9NOOy1r167N0572tBx66KG5+OKLH7f+ta99bU455ZScdNJJ2bBhQ4455piceeaZOfvss5Mk8+bNy7333pu3vOUtueuuu/LUpz41xx57bN73vvclSR577LGceOKJueOOO7J06dIcddRR+chHPrIzvzIAAADAnFLjN9qfy6pqaZL777///ixduvSXzv3sZz/LqlWrsnz58uyyyy6jGXAnmUvfFQAAAGBzHnjggey+++5Jsntr7YGtrfVTUAAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0MFTQQEAAACYcY4687JJu9YV5xzX9Tk71gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6eCpopxtXHrZT/7+VN36j63MXXXRRPvjBD2bt2rU5+OCDc8EFF+RlL3vZJE8HAAAAMPfYsTaLXXbZZTn55JNzxhln5Fvf+lZe9rKX5eijj86aNWtGPRoAAADAjCeszWLnn39+3va2t+X444/PQQcdlAsuuCD77bdfLr744lGPBgAAADDjCWuz1MaNG3PTTTflyCOP/KXjRx55ZK6//voRTQUAAAAwewhrs9Q999yTxx57LHvttdcvHd9rr72ybt26EU0FAAAAMHsIa7NcVf3S+9ba444BAAAAsP2EtVnqqU99aubNm/e43Wnr169/3C42AAAAALafsDZLLVy4MIceemiuvvrqXzp+9dVX58UvfvGIpgIAAACYPeaPegCmzqmnnpo3v/nNWblyZQ4//PB84hOfyJo1a/KOd7xj1KMBAAAAzHjC2ix23HHH5d57780f//EfZ+3atTnkkEPyla98Jfvvv/+oRwMAAACY8YS1Titv/MaoR9gmJ5xwQk444YRRjwEAAAAw67jHGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgw/xRDzBTHXXmZTv1/7vinOO2+zPXXXddPvjBD+amm27K2rVr8/nPfz6ve93rpmA6AAAAgLnHjrVZ7KGHHsrznve8fOxjHxv1KAAAAACzjh1rs9jRRx+do48+etRjAAAAAMxKdqwBAAAAQIeRhrWqOr2qvllVD1bV+qr6QlU9a8KaRVX10aq6p6oeqqovVtXTJ6x5RlV9aXD+nqq6sKoW7txvAwAAAMBcMuoda69I8vEkL0ry6oz9NPWqqlo8tOaCJL+R5A1JXppktyRfrqp5STL4+z+SLB6cf0OS1yf58E76DgAAAADMQSO9x1pr7ajh91X1O0nWJzk0yXVVtXuStyV5c2vtbwdr3pTkx0leleTKJEcmeXaS/Vprdw7WnJbk0qo6o7X2wM76PgAAAADMHaPesTbR7oO/9w3+HppkQZKrxhcM4tl3krx4cOjwJN8Zj2oDVyZZNPg8AAAAAEy6afNU0KqqJOcn+Z+tte8MDu+dZGNr7ScTlt81ODe+5q7hk621n1TVxqE1E/+vRRkLb+OW7OD409JPf/rTfP/739/0ftWqVbnlllvylKc8Jc94xjNGOBkAAADAzDdtwlqSjyV5bsbuk/ZEKkkbet+2Yc2w05OctV3TzUA33nhjjjjiiE3vTz311CTJW9/61lx66aUjmgoAAABgdpgWYa2qPprkPyV5eWvtjqFT65IsrKo9Juxa2zPJ9UNr/t2E6+2RsZ+Q/tJOtiHnZmx33LglSe7YwtrNuuKc47Zn+Ui88pWvTGtbaosAAAAA7IiR3mOtxnwsybFJ/n1rbdWEJTcleTRjTwwd/8w+SQ7Jv4a1ryc5ZHB83JFJNgw+/zittQ2ttQfGX0kenJQvBAAAAMCcMeodax9P8ltJXpvkwaoavyfa/a21R1pr91fVnyX5cFXdm7GHGnwoyW1J/naw9qok/5jkL6vqXUmeMlhziSeCAgAAADBVRv1U0N/P2JNAr02ydug1/DvLU5J8Icmnk3wtycNJXtNaeyxJBn+PSfKzwflPD9b/XzvlGwAAAAAwJ410x1prrbZhzc+SvHPw2tKaNUn+4ySOBgAAAABbNeodawAAAAAwIwlr22guPF1zLnxHAAAAgMkirD2BBQsWJEkefvjhEU8y9ca/4/h3BgAAAGDLRv1U0Glv3rx5WbZsWdavX58k2XXXXVP1hLeGm1Faa3n44Yezfv36LFu2LPPmzRv1SAAAAADTnrC2Dfbee+8k2RTXZqtly5Zt+q4AAAAAbJ2wtg2qKvvss0/23HPPPProo6MeZ0osWLDATjUAAACA7SCsbYd58+aJTwAAAAAk8fACAAAAAOgirAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAh5GGtap6eVV9qarurKpWVa+bcL5t4fWuoTU/2sz5D+z8bwMAAADAXDJ/xP//4iS3JvmLJJ/dzPl9Jrw/OsmfbWbtHyW5ZOj9TydrQAAAAADYnJGGtdba5UkuT5Kq2tz5dcPvq+q1Sb7aWvvhhKUPTlwLAAAAAFNpxtxjrar2SnJMxnasTfSeqrq3qm6pqjOqauETXGtRVS0dfyVZMhUzAwAAADB7jfqnoNvjrUkeTPK5Ccf/S5Kbk/wkyWFJzk2yPMnxW7nW6UnOmoIZAQAAAJgjZlJY+90kf9Va+9nwwdbaR4befruqfpLkM1X1ntbavVu41rlJzh96vyTJHZM6LQAAAACz2owIa1X1siTPSnLcNiy/YfD3mUk2G9ZaaxuSbBi6/o6OCAAAAMAcM1Pusfa2JDe11m7dhrUvGPxdO4XzAAAAADDHjXTHWlXtlrGdZeOWV9Xzk9zXWlszWLM0yf+e5LTNfP7wJC9K8tUk9yd5YZKPJPni+OcBAAAAYCqM+qegKzMWxcaN3/fsk0l+e/DvNySpJP99M5/fkLGfh56VZFGS1UkuSXLeFMwKAAAAAJuMNKy11q7NWDTb2ppPJPnEFs7dnLEdawAAAACwU82Ue6wBAAAAwLQirAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdRhrWqurlVfWlqrqzqlpVvW7C+UsHx4dfN0xYs6iqPlpV91TVQ1X1xap6+s79JgAAAADMNaPesbY4ya1JTtrKmiuS7DP0+t8mnL8gyW8keUOSlybZLcmXq2repE8LAAAAAAPzR/mft9YuT3J5klTVlpZtaK2t29yJqto9yduSvLm19reDY29K8uMkr0py5WTPDAAAAADJ6HesbYtXVtX6qvrnqrqkqvYcOndokgVJrho/0Fq7M8l3krx4J88JAAAAwBwy0h1r2+DyJH+TZHWS5UnOSXJNVR3aWtuQZO8kG1trP5nwubsG5zarqhYlWTR0aMmkTg0AAADArDetw1pr7bKht9+pqhszFtmOSfK5rXy0krStnD89yVk7PiEAAAAAc9VM+CnoJq21tRkLaysGh9YlWVhVe0xYumfGdq1tyblJdh96eYooAAAAANtlRoW1qvo3SfZLsnZw6KYkjyZ59dCafZIckuT6LV2ntbahtfbA+CvJg1M3NQAAAACz0Uh/ClpVuyV55tCh5VX1/CT3DV5nJ/lsxkLaryT5z0nuSfL5JGmt3V9Vf5bkw1V17+AzH0pyW5K/3TnfAgAAAIC5aNT3WFuZ5KtD788f/P1kkt9P8pwkb0myLGNx7atJjmutDe8wOyXJz5N8OsmTk/xdkt9urT02taMDAAAAMJeNNKy11q7N2IMGtuTXt+EaP0vyzsELAAAAAHaKGXWPNQAAAACYLoQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdRhrWqurlVfWlqrqzqlpVvW7o3IKq+tOquq2qHhqs+W9Vte+Ea/xo8Nnh1wd2/rcBAAAAYC4Z9Y61xUluTXLSZs7tmuTXkpwz+HtskgOTfHEza/8oyT5Drz+ZimEBAAAAYNz8Uf7nrbXLk1yeJFU18dz9SV49fKyq3pnkG1X1jNbamqFTD7bW1k3xuAAAAACwyah3rG2v3ZO0JP8y4fh7qureqrqlqs6oqoVbu0hVLaqqpeOvJEumamAAAAAAZqeR7ljbHlW1S5IPJPnr1toDQ6f+S5Kbk/wkyWFJzk2yPMnxW7nc6UnOmqJRAQAAAJgDZkRYq6oFST6VsR12Jwyfa619ZOjtt6vqJ0k+U1Xvaa3du4VLnpvk/KH3S5LcMYkjAwAAADDLTfuwNohqn87YLrR/P2G32ubcMPj7zCSbDWuttQ1JNgz9H5MwKQAAAABzybQOa0NRbUWSI7ayA23YCwZ/107ZYAAAAADMeSMNa1W1W8Z2lo1bXlXPT3JfkjuTfCbJryX5j0nmVdXeg3X3tdY2VtXhSV6U5KtJ7k/ywiQfSfLFCU8NBQAAAIBJNeodayszFsXGjd/37JNJzk7ynwbvb5nwuSOSXJuxn3Mel7EHESxKsjrJJUnOm5JpAQAAAGBgpGGttXZtkq3d4GyrNz9rrd2csR1rAAAAALBTPWnUAwAAAADATCSsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0KErrFXVNVW1bDPHl1bVNTs+FgAAAABMb7071l6ZZOFmju+S5GXd0wAAAADADDF/exZX1XOH3j67qvYeej8vyVFJ/tdkDAYAAAAA09l2hbUktyRpg9fmfvL5SJJ37uhQAAAAADDdbW9YW56kkvwwyWFJ7h46tzHJ+tbaY5M0GwAAAABMW9sV1lprqwf/9DRRAAAAAOa07d2xtklVHZixhxjsmQmhrbX2xzs2FgAAAABMb11hrarenuTiJPckWZexe66Na0mENQAAAABmtd4da+9NckZr7U8ncxgAAAAAmCl675W2R5K/mcxBAAAAAGAm6Q1rf5PkyMkcBAAAAABmkt6fgn4/yTlV9aIktyV5dPhka+3CHR0MAAAAAKaz3rD2fyT5aZJXDF7DWhJhDQAAAIBZrSustdaWT/YgAAAAADCT9N5jDQAAAADmtK4da1X151s731r73b5xAAAAAGBm6L3H2h4T3i9IckiSZUmu2aGJAAAAAGAG6L3H2m9MPFZVT0pyUZIf7uhQAAAAADDdTdo91lprv0jykSSnTNY1AQAAAGC6muyHF/zb9P+8FAAAAABmjN6HF5w/8VCSfZIck+STOzoUAAAAAEx3vbvLXjDh/S+S3J3ktCRbfWIoAAAAAMwGvQ8vOGKyBwEAAACAmWSH7odWVU9L8qwkLck/t9bunpSpAAAAAGCa63p4QVUtrqo/T7I2yXVJ/t8kd1bVn1XVrpM5IAAAAABMR71PBT0/ySuSvCbJssHrtYNjH56c0QAAAABg+ur9Kejrk/xma+3aoWNfqapHknw6ye/v6GAAAAAAMJ317ljbNcldmzm+fnAOAAAAAGa13rD29STvq6pdxg9U1ZOTnDU4BwAAAACzWu9PQU9OcnmSO6rq1ow9FfT5STYkOXKSZgMAAACAaasrrLXWbquqFUnelORXk1SSTyX5q9baI5M4HwAAAACzxI0rD5u8ix192uRdq1NXWKuq05Pc1Vq7ZMLx362qp7XW/nRSpgMAAACAaar3Hmu/l+SfNnP8u0ne0T8OAAAAAMwMvWFt7yRrN3P87iT79I8DAAAAADNDb1j7cZKXbOb4S5Lc2T8OAAAAAMwMvU8F/X+SXFBVC5JcMzj2H5Kcl+TDkzEYAAAAAExnvWHtvCRPSXJRkoWDYz9L8qettXMnYzAAAAAAmM66wlprrSV5T1Wdk+SgJI8kub21tmEyhwMAAACA6ap3x1qSpLX20yTfnKRZAAAAAGDG6H14AQAAAADMacIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoMNKwVlUvr6ovVdWdVdWq6nUTzldVnT04/0hVXVtVB09Ys0dV/WVV3T94/WVVLdu53wQAAACAuWbUO9YWJ7k1yUlbOP/uJKcOzr8wybokV1fVkqE1f53k+UmOGryen+Qvp2pgAAAAAEiS+aP8z1trlye5PEmq6pfO1diBk5O8v7X2ucGxtya5K8lvJfmvVXVQxmLai1pr/zBY8/YkX6+qZ7XW/r+d9V0AAAAAmFtGvWNta5Yn2TvJVeMHWmsbkvx9khcPDh2e5P7xqDZYc0OS+4fWAAAAAMCkG+mOtSew9+DvXROO35Vk/6E16zfz2fVDn3+cqlqUZNHQoSVbWgsAAAAAmzOdd6yNaxPe14RjE89vbs1Ep2dsV9v4644dGRAAAACAuWc6h7V1g78Td57tmX/dxbYuyV6b+ezT8vidbsPOTbL70Ovp/WMCAAAAMBdN57C2KmPh7NXjB6pqYZJXJLl+cOjrSXavqsOG1vy7jMWy67MFrbUNrbUHxl9JHpyC+QEAAACYxUZ6j7Wq2i3JM4cOLa+q5ye5r7W2pqouSPKHVXV7ktuT/GGSh5P8dZK01r5XVVckuaSqfm9wjU8k+bInggIAAAAwlUb98IKVSb469P78wd9PJvntJOcleXKSi5LskeQfkhzZWhveYfbGJBfmX58e+sUkJ03dyAAAAAAw4rDWWrs2Yw8a2NL5luTswWtLa+5L8qZJHg0AAAAAtmo632MNAAAAAKYtYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQIdpH9aq6kdV1Tbz+vjg/LWbOfepUc8NAAAAwOw2f9QDbIMXJpk39P6QJFcn+ZuhY5ck+aOh94/shLkAAAAAmMOmfVhrrd09/L6q/u8kP0jy90OHH26trdupgwEAAAAwp037n4IOq6qFSd6U5M9ba23o1Bur6p6q+m5VfaiqljzBdRZV1dLxV5KtrgcAAACAiab9jrUJXpdkWZJLh479VZJVSdZl7Gei5yZ5XpJXb+U6pyc5a2pGBAAAAGAumGlh7W1JLm+t3Tl+oLV2ydD571TV7UlurKpfa63dvIXrnJvk/KH3S5LcMenTAgAAADBrzZiwVlX7J3lVkmOfYOnNSR5NsmLw78dprW1IsmHo2pM0JQAAAABzxUy6x9rvJFmf5H88wbqDkyxIsnbKJwIAAABgzksjm7gAACAASURBVJoRO9aq6kkZC2ufbK39fOj4v03yxiRfSXJPkmcn+XCSbyX52ghGBQAAAGCOmBFhLWM/AX1Gkj+fcHxjkv+Q5P9MsluSH2dsR9v7WmuP7dQJAQAAAJhTZkRYa61dleRxN0Jrrf04ySt2/kQAAAAAzHUz6R5rAAAAADBtCGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoMH/UAwAAMH0cdeZlk3atK845btKuBQAwHdmxBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgw7QOa1V1dlW1Ca91Q+drsObOqnqkqq6tqoNHOTMAAAAAc8O0DmsD302yz9DrOUPn3p3k1CQnJXlhknVJrq6qJTt7SAAAAADmlvmjHmAb/Ly1tm7iwaqqJCcneX9r7XODY29NcleS30ryX3fqlAAAAADMKTNhx9qKwU89V1XVp6rqgMHx5Un2TnLV+MLW2oYkf5/kxSOYEwAAAIA5ZLrvWPuHJG9J8s9J9kry3iTXD+6jtvdgzV0TPnNXkv23dtGqWpRk0dAhPx0FAAAAYLtM67DWWrt86O1tVfX1JD9I8tYkN4wvm/Cx2syxiU5PctakDAkAAADAnDQTfgq6SWvtoSS3JVmRsQcVJP+6c23cnnn8LraJzk2y+9Dr6ZM4JgAAAABzwIwKa4OfcB6UZG2SVRmLa68eOr8wySuSXL+167TWNrTWHhh/JXlw6qYGAAAAYDaa1j8FraoPJflSkjUZ24n23iRLk3yytdaq6oIkf1hVtye5PckfJnk4yV+PaGQAAAAA5ohpHdYy9hPN/57kqUnuzth91V7UWls9OH9ekicnuSjJHhl72MGRrTU70AAAAACYUtM6rLXW3vAE51uSswcvAAAApqGjzrxs0q51xTnHTdq1AHbUjLrHGgAAAABMF8IaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0ENYAAAAAoIOwBgAAAAAdhDUAAAAA6CCsAQAAAEAHYQ0AAAAAOghrAAAAANBBWAMAAACADsIaAAAAAHQQ1gAAAACgg7AGAAAAAB2ENQAAAADoMH/UA0xXN648bNKutfLGb0zatQAAAACYHuxYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHYQ1AAAAAOggrAEAAABAB2ENAAAAADoIawAAAADQQVgDAAAAgA7CGgAAAAB0mD/qAQAAAHamo868bNKudcU5x03atQCYeexYAwAAAIAOwhoAAAAAdBDWAAAAAKCDsAYAAAAAHTy8AAAARsiN9AFg5rJjDQAAAAA6CGsAAAAA0MFPQXcC2/sBAAAAZh871gAAAACgg7AGAAAAAB2ENQAAAADoIKwBAAAAQAdhDQAAAAA6CGsAAAAA0EFYAwAAAIAOwhoAAAAAdJjWYa2qTq+qb1bVg1W1vqq+UFXPmrDm2qpqE16fGtXMAAAAAMwN0zqsJXlFko8neVGSVyeZn+Sqqlo8Yd0lSfYZev3ezhwSAAAAgLln/qgH2JrW2lHD76vqd5KsT3JokuuGTj3cWlu3M2cDAAAAYG6b7jvWJtp98Pe+CcffWFX3VNV3q+pDVbVkaxepqkVVtXT8lWSr6wEAAABgomm9Y21YVVWS85P8z9bad4ZO/VWSVUnWJTkkyblJnpexn45uyelJzpqiUQEAAIBOR5152aRc54pzjpuU68DWzJiwluRjSZ6b5KXDB1trlwy9/U5V3Z7kxqr6tdbazVu41rkZi3TjliS5YzKHBQD+//buPVqWsj7z+PdBLgooIoYAKoMSRCVmUBEGlMugRLwE0WhwNBqQDBHiGEZ0DVmOE1wkogtvA2jCGBIjoxEjCohczhCDEQH1AKJEbrpUkJvc7x4ueeePt7Y0ffbu7t1uuqr2+X7W6rV3d1X3fs57quvX/db7VkmSJEnLWy861pIcC+wD7FZKGdcBdjHwILBN8/tqSimrgFUDr79ESSVJkiRJkrSm6HTHWjP981jgdcAepZSfTPC07YB1gBsey2ySJEmSJElzlmoKK8x+GqvTb6fX6Y414JPAm4HXAncn2ax5/M5Syv1JtgbeApwB3AI8D/gocAnwrRbySpIkSZIkaQ3R9auCHky9Eui51BFoc7e5LtAHgJcBZwNXAscAK4CXl1IennVYSZIkSZIkrTk6PWKtlDLy5GellGuB3WcUR5IkaWJOqZAkSVr+uj5iTZIkSZIkSeqkTo9YkyRJkiRJi9fnE+lLfeKINUmSJEmSJGkKdqxJkiRJkiRJU3AqqCRJ6iynsUiSJKnLHLEmSZIkSZIkTcGONUmSJEmSJGkKTgWVJEmSpJ5YqinyTo+fnG0uaRRHrEmSJEmSJElTcMSaJEmSJGk1K3fYcele7JWHLd1rSVKHOGJNkiRJkiRJmoIda5IkSZIkSdIU7FiTJEmSJEmSpmDHmiRJkiRJkjQFO9YkSZIkSZKkKXhVUEmSJrT3+09astc668j9luy1JKktS7VfdJ8oSeorR6xJkiRJkiRJU7BjTZIkSZIkSZqCU0G1LM16utbKHXZcsr+3w8rvLNlrSZIkSZKkx44j1iRJkiRJkqQpOGJN6hhPAixJWqylHDnNKw9buteaMWuoJEmaNUesSZIkSZIkSVOwY02SJEmSJEmagh1rkiRJkiRJ0hTsWJMkSZIkSZKmYMeaJEmSJEmSNAWvCipJmjmv3CdJkiRpOXDEmiRJkiRJkjQFR6xJUk8t1agvcOSXJEmSJE3DEWuSJEmSJEnSFOxYkyRJkiRJkqbgVFBJS8JpiZKkaazcYcele7FXHrZ0ryVJWhT351pTOWJNkiRJkiRJmoIda5IkSZIkSdIUnAq6DC3lENwdVn5nyV5LkiRJkmbBaYmalNuKfl2OWJMkSZIkSZKm4Ig1SZIkSZ3nqBJJUhc5Yk2SJEmSJEmagh1rkiRJkiRJ0hScCqqR9n7/SUvyOmcdud+SvI6k9jgFp9/cn0uS1H1+3pL6xxFrkiRJkiRJ0hTsWJMkSZIkSZKm4FRQSWs8p8hJkiRJkqbhiDVJkiRJkiRpCnasSZIkSZIkSVNwKqgkSVpSXtFM6jbfo5K0PLg/7wZHrEmSJEmSJElTcMSapF7y6IzWBG7ns2eba1JuK5IkCRyxJkmSJEmSJE3FjjVJkiRJkiRpCk4FlaQZcurQ7NnmkqS2WYskaflyxJokSZIkSZI0BTvWJEmSJEmSpCk4FVSd4RB5SZIkSZLUJ45YkyRJkiRJkqbgiDVpDeYoQUmSJEmSprdsRqwlOSTJT5L8MslFSXZtO5MkSZIkSZKWr2XRsZZkP+ATwF8BLwC+CZyZZMtWg0mSJEmSJGnZWhYda8C7gRNKKX9bSrm8lHIocC1wcMu5JEmSJEmStEz1vmMtybrAi4AVQ4tWALvMPpEkSZIkSZLWBMvh4gVPBR4H3DT0+E3AZvM9Icl6wHoDDz0R4K677vrVA/c8/PCSBXxo1X1L9lqDGRfSxex9zQ39zd7X3NDf7H3NDf3N3tfc0N/sfc0N/c3e19zQ3+x9zQ39zd7X3NDf7H3NDf3N3tfc0N/sfc0N/c3e19zw6OyT/DvmpJSyZCHakGQL4Dpgl1LKBQOPvw94aynlOfM85wjgL2YWUpIkSZIkSX3z9FLKdaNWWA4j1m4BHmb10WmbsvootjlHAR8beuwpwG1LGw2oo+F+DjwduPsxeP3HUl+z9zU39Dd7X3NDf7P3NTf0N3tfc0N/s/c1N/Q3e19zQ3+z9zU39Dd7X3NDf7P3NTf0N3tfc0N/s/c1N/Q3+2Od+4nA9eNW6n3HWinlgSQXAXsBXxlYtBdw6gLPWQWsGnp48nF+i5Bk7te7SymPyd94rPQ1e19zQ3+z9zU39Dd7X3NDf7P3NTf0N3tfc0N/s/c1N/Q3e19zQ3+z9zU39Dd7X3NDf7P3NTf0N3tfc0N/s88g90Sv2fuOtcbHgBOTrAQuAA4CtgT+ptVUkiRJkiRJWraWRcdaKeWkJJsA/wvYHLgMeFUp5WftJpMkSZIkSdJytSw61gBKKZ8CPtV2jnmsAj7A6lNP+6Cv2fuaG/qbva+5ob/Z+5ob+pu9r7mhv9n7mhv6m72vuaG/2fuaG/qbva+5ob/Z+5ob+pu9r7mhv9n7mhv6m70TuXt/VVBJkiRJkiSpDWu1HUCSJEmSJEnqIzvWJEmSJEmSpCnYsSZJkiRJkiRNwY41SZIkSZIkaQp2rC2RJLsl+WqS65OUJPsOLFsnyYeT/CDJvc06n02yRZuZm2wL5m6WH5Hkiib37UnOSbJTW3kHjcs+tO7xzTqHzjLjAlnGtflnmscHbxe2lXfQJG2e5LlJTktyZ5K7k1yYZMs28g5kGtfmw+09d3tvW5kHso3LvmGS45L8PMn9SS5PcnBbeQdyjcv9m822fn2S+5KclWSbtvIO5PrzJN9ttt1fJDklybZD66yX5NgktzT7xtOSPL2tzAO5Jsl+UJJzk9zV/L88ua28A5lG5k7ylKa9r2y2lWuSHJNkozZzN9kmafPjk/y4eX/enOTUJM9pK3OTaWzugXWT5MxxdXZWJmzzc+fZn3+hrcxNponaPMnOSb7e7FvuaP4tT2gj80Cmce/RrUbU0Td2NXezzmZJTkxyY9PmFyd5Q1uZB3JNkn3rJF9p9it3Jflikt9sK3OT6eAk32/y3JXkgiSvHFjeyfoJE2XvXP2E0bm7XD9hojbvXP1sco3MPbBep+onTNTmnaufTa6xbd52/bRjbelsAFwKvHOeZesDLwSObH6+Hng2cNrM0i1sVG6Aq5plzwdeCvwUWJHkN2aSbrRx2QFodmQ7AdfPItQEJsl9FrD5wO1VM8g1iZHZk2wNnAdcAewB/Efqdv/LGeVbyLg233zo9nagACfPJN1o47J/HNgb+EPguc39Y5O8djbxFrRg7iQBTgGeBbwWeAHwM+CcJBvMMuQ8dgc+CfwnYC9gbeo+bzDXJ4DXAW+i7hc3BE5P8rgZZx02Sfb1qfuXD84+3oLG5d6iub2HWov2p27zJ8w86eomafOLgAOo789XAGnWaXN7mST3nEOp+8OumDT7p3n0fv1PZhlyHmNzJ9mZ+v5cAewIvBg4Dvj3mad9tHHZr2X1OvoXwL3AmTNP+4hJtpUTgW2Bfaj7ly8DJyV5wYyzDhuZvfm5gvre3BN4CbAu8NUkbX6/+zlwOLBDc/s6cGqS7ZrlXa2fMD57F+snjM7d5foJ49u8i/UTxuee07X6CZNl71r9hDG5O1E/SynelvhGfQPtO2adFzfrbdl23kXmflKz3svazjtJduBp1DfidtROwUPbzjouN/AZ4JS2s02Z/QvAiW1nm2ZbGVrnFOCf2846YZtfBrx/6LGLgCPbzrtQbuqBhQJsN/DY44BbgT9uO+9Q9t9osu7W3N8IeADYb2CdLYCHgVe0nXdU9qFlezTLntx2zsXkHljnjcAqYO22806R/XeadbZuO++43NSDI9cCm02y7+xKduBc4BNtZ5si94Vd2ncvdnsZWucS4IS2s07Q5vcAbx1a71bgwLbzjsoO/G5Td540sM7GzTovbzvvUPbbgAP7VD+Hsw891tn6OSr3wLJO1s8Js3eufi6Uuw/1c77sfaifC+RuvX46Yq09G1HfZHe0HWRSSdYFDgLupI5E6bTmiN2JwNGllH9rO88i7ZE69P+qJJ9OsmnbgcZp2vvVwFVJzm7yf7srQ58nlTqN4tV052jeOOcB+yR5WjPk/D9TO67ObjnXKOs1P381krGU8jD1A/dLW0m0sLnpErc1P18ErEM9IgZAKeV6agfnLrONNtZw9r6YJPdGwF2llIdmkGcxRmZvRpkcAPyE+oG7K1bLnWR94B+Bd5ZSbmwl1WQWavO3pE43+7ckH0nyxFkHG+NRuZs6vxPwiyTnJ7kpyTeSdG2fCOO38xcB29O9Ojpf7vOA/Zopc2sleRO1Rp0763BjDGdfj/o9YtXAOr+kjs7oxDaT5HFNe24AXECP6uc82XthwtydrJ/jsne1fs6Xuy/1c0Sbd7p+DufuSv20Y60FSR4PfAj4fCnlrrbzjJPkNUnuoRbs/w7sVUq5peVYk/gfwEPAMW0HWaQzgbdQh/YfRh3d+PUk6418Vvs2pQ7pP5w6FPd3ga8AX06ye5vBFumPgLup00H64F3AD6kjMx+gtv0hpZTzWk012hXUqZ9HJdk4ybpJDqce1du83WiPaKasfgw4r5RyWfPwZsADpZTbh1a/qVnWCQtk77xJcifZBHg/cPwss40zKnuSQ5o6eg91Gs5epZQHWoi5mhG5Pw6cX0o5tZ1k443I/jngv1BHlhwJ/D4d2qcvkPtZzc8jqNNw9gYuBv45HTj/5JwJ9y0HApeXUs6fXbLRRuTejzrN8lZqJ9XxwOtKKT+efcr5LZD9QupU2w8nWb/pdDia+t2u1Tqa5PnN/m4V8DfU9vwhPaifI7J32qS5u1g/x2Xvav0ck7vT9XNM9s7WzxG5O1E/157VH1KVZB3qdLm1gENajjOpf6EeeXwq8F+BLybZqZTyi3ZjLaw5WvpnwAtLMz60L0opJw3cvSzJSmonxKvpyI5tAXMd9aeWUj7e/P69JLsA7wC+0U6sRXs78LlSStvnhZvUu6jnYNmHup3sBnwqyQ2llHNaTbaAUsqDSX6fOprhNuo0kHNo91w88zmOOu1gkiNeoVvn0VhM9i4ZmTvJk4CvUTuTPzDDXJMYlf1zwP+jfuF9D7WOvqQj+5nVcifZh3pwp+3zTI0zb5uXUj49cPeyJFcDK5O8sJRy8SwDLmC+3HM19PhSyt83v1+S5GXUuvTnM8w3yrj36BOAN1O/kHXJQrn/kjqF8uXALcC+wD8l2bWU8oPZRlzQatlLKTenXhjir6mfA/6dOkLmYmpNbdOV1O8NT6Z+Kf+HMQdYu1Q/583eg861sbk7XD/HZe9q/VxoO/8tul8/F2zzjtfPhdq8E/XTjrUZajrVvgg8E9izD6PVAEop9wI/am4XNm+wA4GjWg022q7UEVTX1AN9QD2H00eTHFpK2aqtYItVSrkhyc+AzhyxXsAt1BGCwx8+LqcnX+6T7Eo9ifF+bWeZRPMF5oPUIzZfax7+fpLtqR8+OtmxBlBKuQjYPvXKVOs2XxK+DaxsORoASY6ldlbuVkr5+cCiG4F1k2w8dNR9U6ATozNGZO+0cbmbqQhnUY9av66U8uCMIy5oXPZSyp3U0yhcnXqV59upJ/D+x5kGHTIi957A1sAdAzUU4OQk3yyl7DG7lPNb5HZ+MfAgtY62+sVgRO4bmp/z1dBWr6w9Z8I2fwP1JO+fnVmwMRbKnXrBpXcCvz1wypBLm88Cf0o9KNiqUW1eSlkBbJ3kqcBDpZQ7ktxInSrXmmY00Y+auyuTvJh6sPskOl4/R2TvwsnbFzQud5fr57jsXa2fI3LfT8fr5yK3887UzxG5P9Q81mr9dCrojAx0qm1DPanorS1H+nWER86R1FUnUo/ubT9wu546TP4VLeZatGbY9jN45EN3JzU7u+9SO6YGPZs6kqoPDgQuKqV0/hyCjXWa2/AVbx6mJ/v3UsqdTafaNtSr/LQ6bD7VcdSrN+9ZShn+gnIR9QPGXgPP2Rz4bVr+YjBB9k6aJHdzpH0FdbrzPh04Ug38Wm3eah2dIPeHWL2GQj0dxAEzCzqPKdt8O+q+srU6OkHun1I/p3Suhi6yzQ8ETiul3DybdAubIPf6zc/O1dDFtHkp5ZamU21PaifVabPKOaG5/V1n6+cIffjOM59f5e5q/RxhXJt39f9kLldn6+cIo9q09fo5wlzun9KB+umItSWSZEPq0M85z2xGjdxG/Y/+EvBC4DXA45LMnUvgtjbniY/JfSvwPmqBvgHYhDp99enAP8046mpGZS+lXEPNP7j+g8CNpZQrZxhzNWPa/Dbq/PCTqW2+FXVE0i3U85W1aoI2P5p6mfp/pU4h3hv4Peo8/dZMkHvug8cbqee164xx2ZN8Azg6yf3U4rE78Dbg3bNP+4gJcr8RuBm4hnoJ+P9NvRruitVfbaY+SZ3G9Frg7oF99Z2llPtLKXcmOYE6+vVW6nv2I8APaH+E4MjsAM1jm/HI/83zk9wNXFNKaesiByNzN0faV1C/BP8h8KTm/Qpwc6kXvmjLuOzPoo6AXUHd3p9GPf/n/cAZLeSdM247v5E6OvNXmiPv13Sgw3Zcm29NPU/pGdTa+Tzgo9SrVH6rhbxzxrV5SXI08IEklwLfo57z8znUUWBtGrtvAUjyW9TTEbxq9hHnNS73FdTRD8cneQ/1c+O+1I6f17SQd9Ak+/MDqCMybgZ2ptbRj7f5OTfJB6mndbgWeCLwJupnwL07Xj9HZm+Wd7F+jszd8fo5LntX6+e47bzL9XNcm3e1fo5r827Uz9KBS6UuhxuPXHp5+PYZaufIfMsKsEeHcz+eek6v66gnCbyeOprkxW2397jsC6z/U+DQLucGnkC9muMvqEeWftY8/oy2c0/a5tS57FdTC9/3gNf2JPdBwH3ARm3nXUx26oe8v2/ep3NfFN4NpOO530UtjnPb+ZHUKaFtt/dC++r9B9Z5PHAs9UvYfcBXu/AenTD7EePW6VruEdtSAbbqcpsDW1A/oN7UbOvXUs8Xs22Xc494zr5t5p6wzZ9BPafn3Mnof0TtcHhKl3MPrHd4s53cSx3F89Kut/nAeh9ssq/VduZJc1NnkpzcvEfvpV71/q09yf4h6hf4B4Cr6EbtP4H6eXsV9bPsOdSTzc8t72T9nDD7EYvdb7admw7Xzwmyd7J+TrKtzLN+J+rnBG3eyfo5aZvTcv1ME0KSJEmSJEnSIvTiHDySJEmSJElS19ixJkmSJEmSJE3BjjVJkiRJkiRpCnasSZIkSZIkSVOwY02SJEmSJEmagh1rkiRJkiRJ0hTsWJMkSZIkSZKmYMeaJEmSJEmSNAU71iRJkjokyS5JHk5yVgt/+9wkJcnh8yw7o1l2xKxzSZIkdZUda5IkSd3yduBY4KVJtmzh718LHDD4QJItgD2BG1rII0mS1Fl2rEmSJHVEkg2APwD+Gjgd2H9o+T5Jrk5yf5J/SfJHzSiyJw+ss0uSf23WuTbJMc3rTup0YJMkLxl4bH9gBfCLoTwbJ/lsktuT3JfkzCTbDCzfP8kdSV6R5PIk9yQ5K8nmA+vskeQ7Se5t1v1Wkv+wiLySJEmtsWNNkiSpO/YDriylXAn8X+CAJAFIshXwJeAUYHvgeOCvBp+c5PnA2cCXgd9pXu+lwHGLyPAA8DkePWptf+Dv5ln3M8AOwD7AzkCAM5KsM7DO+sB7gLcCuwFbAh9p8q7d/Hu+0eTdGfg/QFlEXkmSpNbYsSZJktQdB1I71ADOAjYEXtbcfwe10+29pZQrSylfoHZsDXov8PlSyidKKVeXUs4H3gW8LcnjF5HjBOAPkmyQZDdgI+Brgys0I9P2Af64lPLNUsqlwFuApwH7Dqy6DvCOUsrKUsrF1E6+uX/Tk5rXPr2U8uNSyuWllH8opVyziKySJEmtsWNNkiSpA5JsC+wIfAGglPIQcBL1nGsA2wLfHXrad4buvwjYv5lyeU+Se6gj2NYCnjlpllLK94GrgTc0f//EUsqDQ6s9F3gI+PbA824FrmyWzbmvlPLjgfs3AJs2699G7Rw8O8lXk/zZ4DRRSZKkrlu77QCSJEkC6mi1tYHrmtmfUKdWPphk4+b34SmSGbq/FnWK6DHzvP5iR4H9HfCnwPOoHX7Dhv/24OODOYc75Mrgc0spByQ5BtibOnX1L5PsVUq5cJF5JUmSZs6ONUmSpJY15xp7G3AY9SIBg06mTrG8AnjV0LIdhu5fDGxXSvnREsT6PPVcaJeWUn44z/IfUj9L7gScD5BkE+DZwOWL+UOllEuAS4CjklwAvBmwY02SJHWeHWuSJEntew2wMXBCKeXOwQVJvkQdzfZ64N1JPkw9B9r2PHLV0LkRYh8GLkzySeDTwL3UaZl7lVL+22IClVJub6ZlDo84m1t+dZJTgU8n+RPgbuBDwHXAqZP8jSTPBA4CTgOup053fTbw2cVklSRJaovnWJMkSWrfgcA5w51qjZOpnWgbU8959nrg+8DBPHJV0FXwq3Oj7Q5sA3yTOgrsSOp5zRatlHJHKeXeEascAFwEnA5cQJ3i+ap5zse2kPuA51D/jVdRrwh6HHU6qyRJUuelFK9mLkmS1EdJ3ke94uYz2s4iSZK0JnIqqCRJUk8kOYR6ZdBbgZcA76WO8JIkSVIL7FiTJEnqj22A/wk8hXqVz48CR03yxCS7AmcutLyUsuFSBJQkSVqTOBVUkiRpDZDkCcDTFlq+RFcSlSRJWqPYsSZJkiRJkiRNwauCSpIkSZIkSVOwDEeFNAAAAE5JREFUY02SJEmSJEmagh1rkiRJkiRJ0hTsWJMkSZIkSZKmYMeaJEmSJEmSNAU71iRJkiRJkqQp2LEmSZIkSZIkTcGONUmSJEmSJGkK/x8pBpET4dItHgAAAABJRU5ErkJggg==\n",
      "text/plain": [
       "<Figure size 1500x800 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,8), dpi=100)\n",
    "sns.countplot(x='Age_Mons',hue='Class',data=asd_data, palette='Set1')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x18fabed1348>"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAA+0AAAJPCAYAAAAJ5DVCAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAAPYQAAD2EBqD+naQAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nOzde7RdZX3/+8/XAFEgISBisICFCoqoxRNEUfFyqgiHekF7hvzqrf2JVhH741L1h0hFLUfrBTmoWKW2emhVtFWrVAEvpbZcVMALKLaglEghiYAG5G58zh9r7bDY7ECys/deT5LXa4w59l5zPmuuZ2XAyHjnmWuuaq0FAAAA6M8Dxj0BAAAAYGqiHQAAADol2gEAAKBToh0AAAA6JdoBAACgU6IdAAAAOiXaAQAAoFObjXsCPaiqSvKwJDePey4AAABsMhYkuba11tY0QLQPPCzJNeOeBAAAAJucnZL895oOivaBm5PkZz/7WRYuXDjuuQAAALCRu+mmm7Lzzjsn93PFt2gfsXDhQtEOAABAN9yIDgAAADol2gEAAKBToh0AAAA65TPtAAAAjMWqVaty1113jXsas2LzzTfPvHnz1vs8oh0AAIA51VrLsmXL8stf/nLcU5lVixYtyuLFi1NV0z6HaAcAAGBOTQT7DjvskC233HK9orZHrbXceuutWbFiRZJkxx13nPa5RDsAAABzZtWqVauD/cEPfvC4pzNrHvSgByVJVqxYkR122GHal8q7ER0AAABzZuIz7FtuueWYZzL7Jt7j+nxuX7QDAAAw5za2S+KnMhPvUbQDAABAp0Q7AAAAdEq0AwAAsFGoqnzhC18Y9zRmlGgHAABgg7Bs2bK8/vWvz2677Zb58+dn5513znOf+9x8/etfH/fUZo2vfAMAAKB7//Vf/5WnPOUpWbRoUd797nfncY97XO66666cffbZed3rXpcf//jH457irLDSDgAAQPcOP/zwVFW+/e1v5w/+4A+yxx57ZK+99srRRx+dCy+8cMrnvOlNb8oee+yRLbfcMrvttluOP/74e3z92ve///0885nPzIIFC7Jw4cIsWbIkF110UZLk6quvznOf+9xsu+222WqrrbLXXnvly1/+8py811FW2gEAAOjajTfemLPOOisnnnhittpqq3sdX7Ro0ZTPW7BgQT7+8Y/nYQ97WC699NK86lWvyoIFC/LGN74xSfKSl7wkj3/84/PhD3848+bNy/e+971svvnmSZLXve51ufPOO/PNb34zW221VX70ox9l6623nr03uQaiHQAAgK5deeWVaa3lUY961Do97y1vecvq33/7t387xxxzTM4444zV0b506dK84Q1vWH3e3XffffX4pUuX5kUvelEe+9jHJkl222239X0b0+LyeAAAALrWWksyuDv8uviHf/iHPPWpT83ixYuz9dZb5/jjj8/SpUtXHz/66KNz2GGH5VnPelbe9a535Sc/+cnqY3/6p3+av/iLv8hTnvKUvPWtb80PfvCDmXkz60i0AwAA0LXdd989VZXLL798rZ9z4YUX5tBDD81BBx2UM888M9/97ndz3HHH5c4771w95oQTTsgPf/jDHHzwwfnGN76RRz/60fn85z+fJDnssMPy05/+NC972cty6aWXZp999skHPvCBGX9v90e0AwAA0LXtttsuz3nOc/KhD30ot9xyy72O//KXv7zXvvPOOy8Pf/jDc9xxx2WfffbJ7rvvnquvvvpe4/bYY48cddRROeecc/LCF74wf/u3f7v62M4775zXvOY1+dznPpdjjjkmp5122sy+sbUg2gEAAOjeqaeemlWrVmXffffNP/7jP+aKK67I5ZdfnlNOOSX77bffvcY/4hGPyNKlS/PpT386P/nJT3LKKaesXkVPkttuuy1HHHFEzj333Fx99dU577zz8p3vfCd77rlnkuTII4/M2WefnauuuiqXXHJJvvGNb6w+NpfciA4AAIDu7brrrrnkkkty4okn5phjjsl1112XhzzkIVmyZEk+/OEP32v885///Bx11FE54ogjcscdd+Tggw/O8ccfnxNOOCFJMm/evNxwww15+ctfnuXLl2f77bfPC1/4wrztbW9LkqxatSqve93rcs0112ThwoU58MAD8/73v38u33KSpCY+0L8pq6qFSVauXLkyCxcuHPd0gEkOPP6McU8BZt1Z73jxuKcAAHPi9ttvz1VXXZVdd901D3zgA8c9nVl1X+/1pptuyjbbbJMk27TWblrTOVweDwAAAJ0S7QAAANAp0Q4AAACdEu0AAADQKdEOAAAAnRLtAAAA0KmxR3tV/VZV/V1V3VBVt1bV96pqycjxqqoTquraqrqtqs6tqr0mnWPbqjq9qlYOt9OratHc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\n",
      "text/plain": [
       "<Figure size 1200x700 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(12,7), dpi=100)\n",
    "sns.countplot(x='Family_mem_with_ASD',hue='Class',data=asd_data, palette='Set1')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Train Test Split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>A1</th>\n",
       "      <th>A2</th>\n",
       "      <th>A3</th>\n",
       "      <th>A4</th>\n",
       "      <th>A5</th>\n",
       "      <th>A6</th>\n",
       "      <th>A7</th>\n",
       "      <th>A8</th>\n",
       "      <th>A9</th>\n",
       "      <th>A10</th>\n",
       "      <th>Age_Mons</th>\n",
       "      <th>Sex</th>\n",
       "      <th>Jaundice</th>\n",
       "      <th>Family_mem_with_ASD</th>\n",
       "      <th>Who_completed_the_test</th>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>Case_No</th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "      <th></th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <td>534</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>13</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>532</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>12</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>670</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>14</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>324</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>32</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>634</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>24</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>340</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>36</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>694</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>27</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>172</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>525</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>20</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <td>205</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>36</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "         A1  A2  A3  A4  A5  A6  A7  A8  A9  A10  Age_Mons  Sex  Jaundice  \\\n",
       "Case_No                                                                     \n",
       "534       1   1   1   1   1   1   1   1   1    0        13    0         1   \n",
       "532       1   1   1   1   1   0   1   1   1    1        12    1         0   \n",
       "670       1   1   0   1   1   1   1   0   1    0        14    0         0   \n",
       "324       1   1   1   1   1   1   1   1   1    1        32    0         1   \n",
       "634       1   0   0   1   1   0   0   0   0    1        24    0         1   \n",
       "340       1   0   1   1   1   1   1   1   1    1        36    0         0   \n",
       "694       1   1   1   1   1   1   1   1   0    1        27    0         1   \n",
       "172       0   1   1   1   1   0   1   0   1    1        23    0         0   \n",
       "525       1   1   1   1   1   1   1   1   1    1        20    1         0   \n",
       "205       1   1   1   1   0   1   1   1   0    0        36    0         1   \n",
       "\n",
       "         Family_mem_with_ASD  Who_completed_the_test  \n",
       "Case_No                                               \n",
       "534                        0                       0  \n",
       "532                        0                       0  \n",
       "670                        0                       0  \n",
       "324                        0                       0  \n",
       "634                        0                       0  \n",
       "340                        0                       0  \n",
       "694                        1                       0  \n",
       "172                        0                       0  \n",
       "525                        0                       0  \n",
       "205                        0                       0  "
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = asd_data.drop('Class', axis=1)\n",
    "y = asd_data['Class']\n",
    "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=101)\n",
    "X_train.head(10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [],
   "source": [
    "X_train.to_excel('Traning_Testing2/X_train.xlsx', index=False)\n",
    "X_test.to_excel('Traning_Testing2/X_test.xlsx', index=False)\n",
    "y_train.to_excel('Traning_Testing2/y_train.xlsx', index=False)\n",
    "y_test.to_excel('Traning_Testing2/y_test.xlsx', index=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Training the Random Forest model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report,confusion_matrix,accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [],
   "source": [
    "rfc = RandomForestClassifier(n_estimators=600)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [],
   "source": [
    "rfc = rfc.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Predictions and Evaluation of RF Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions_rf = rfc.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overall accuracy of ADA model using test-set is : 96.208531\n"
     ]
    }
   ],
   "source": [
    "acc_rf = accuracy_score(y_true=y_test, y_pred= predictions_rf)\n",
    "print(\"Overall accuracy of ADA model using test-set is : %f\" %(acc_rf*100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.99      0.91      0.95        78\n",
      "           1       0.95      0.99      0.97       133\n",
      "\n",
      "    accuracy                           0.96       211\n",
      "   macro avg       0.97      0.95      0.96       211\n",
      "weighted avg       0.96      0.96      0.96       211\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,predictions_rf))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 71   7]\n",
      " [  1 132]]\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y_test,predictions_rf))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Skill: ROC AUC=0.500\n",
      "RF: ROC AUC=0.997\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import roc_curve\n",
    "from sklearn.metrics import roc_auc_score\n",
    "from matplotlib import pyplot\n",
    "\n",
    "lr_probs = rfc.predict_proba(X_test)\n",
    "ns_probs = [0 for _ in range(len(y_test))]\n",
    "lr_probs = lr_probs[:, 1]\n",
    "\n",
    "# calculate scores\n",
    "ns_auc = roc_auc_score(y_test, ns_probs)\n",
    "lr_auc = roc_auc_score(y_test, lr_probs)\n",
    "\n",
    "# summarize scores\n",
    "print('No Skill: ROC AUC=%.3f' % (ns_auc))\n",
    "print('RF: ROC AUC=%.3f' % (lr_auc))\n",
    "\n",
    "# calculate roc curves\n",
    "ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)\n",
    "lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)\n",
    "\n",
    "# plot the roc curve for the model\n",
    "pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')\n",
    "pyplot.plot(lr_fpr, lr_tpr, marker='.', label='RF')\n",
    "\n",
    "# axis labels\n",
    "pyplot.xlabel('False Positive Rate')\n",
    "pyplot.ylabel('True Positive Rate')\n",
    "\n",
    "# show the legend\n",
    "pyplot.legend()\n",
    "\n",
    "# show the plot\n",
    "pyplot.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Training the Adaboost model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import AdaBoostClassifier\n",
    "from sklearn.metrics import classification_report,confusion_matrix,accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [],
   "source": [
    "ada = AdaBoostClassifier(n_estimators=500)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "AdaBoostClassifier(algorithm='SAMME.R', base_estimator=None, learning_rate=1.0,\n",
       "                   n_estimators=500, random_state=None)"
      ]
     },
     "execution_count": 45,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "ada.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Predictions and Evaluation Ada Model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [],
   "source": [
    "prediction_ada = ada.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overall accuracy of ADA model using test-set is : 100.000000\n"
     ]
    }
   ],
   "source": [
    "acc_ada = accuracy_score(y_true=y_test, y_pred= prediction_ada)\n",
    "print(\"Overall accuracy of ADA model using test-set is : %f\" %(acc_ada*100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       1.00      1.00      1.00        78\n",
      "           1       1.00      1.00      1.00       133\n",
      "\n",
      "    accuracy                           1.00       211\n",
      "   macro avg       1.00      1.00      1.00       211\n",
      "weighted avg       1.00      1.00      1.00       211\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,prediction_ada))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 78   0]\n",
      " [  0 133]]\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y_test,prediction_ada))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 50,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "No Skill: ROC AUC=0.500\n",
      "ADA: ROC AUC=1.000\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAYIAAAEGCAYAAABo25JHAAAABHNCSVQICAgIfAhkiAAAAAlwSFlzAAALEgAACxIB0t1+/AAAADh0RVh0U29mdHdhcmUAbWF0cGxvdGxpYiB2ZXJzaW9uMy4xLjEsIGh0dHA6Ly9tYXRwbG90bGliLm9yZy8QZhcZAAAgAElEQVR4nO3dd3hUZfbA8e9JKKFDCJ2EhN5EwRBEQUVQERUUG/a6rK5l7WJZF+v6c1VWV1fFiq4L7lIUe6WJdBAIAZQSSEApAUIJCSnn98cdMISQTMjcmczc83mePOSWmXvuZJgz7/vee15RVYwxxnhXVKgDMMYYE1qWCIwxxuMsERhjjMdZIjDGGI+zRGCMMR5XLdQBVFRcXJwmJiaGOgxjjAkrixYt2q6qTUrbFnaJIDExkYULF4Y6DGOMCSsisuFo26xryBhjPM4SgTHGeJwlAmOM8ThLBMYY43GWCIwxxuNcSwQi8raIbBWR1KNsFxF5SUTWiMgyEenlVizGGGOOzs0WwbvA4DK2nwN08P2MBF51MRbImA+znnf+LW25vP2rsorGGsxzq8qvs5uxVfa8Avm6hNN7uSS339vh9Nq4GKtr9xGo6kwRSSxjl2HAe+rUwZ4rIg1FpIWq/hrwYDLmwztDoCgfJAoaJcHO9aBFznKz7lCz/u/75+2GLalH316VVDTWYJ5beccK5evsZmyVPa9Avi7h9F4uye33dhi9NoW52URtXYGoQrUYuHYqxKcE7PlDOUbQCsgotpzpW3cEERkpIgtFZOG2bdsqfqT0WU4SAOePnpPl/HtwOTf78P1zs8veXpVUNNZgnlt5xwrl6+xmbJU9r0C+LuH0Xi7J7fd2mLw22fvz2bJ1iy9WhcIDzmdaAIXyzmIpZV2ps+So6lhgLEBycnLFZ9JJ7O9kfC2CarVg0GPw5SjnBY2uARe9eXh2zZgP44YefXtVUtFYg3lu5R0rlK+zm7FV9rwC+bqE03u5JLff21X8tcnen8/fPl/JhNUZDGm4kX/mjya6KN+JNbF/QI8lbs5Q5usa+lRVu5ey7XVguqqO9y2vBk4vr2soOTlZj6nExGv9nYx/8I+dMd/Jqon9S//jl7e9KqlorME8t6r8OrsZW2XPK5CvSzi9l0ty+71dRV+bwiLl7H/MZN22vfzh1LbcNagjMb8tqlSsIrJIVZNL3RbCRHAucBswBOgDvKSq5Z7dMSeCd851/r3+s4o/1hhjgmDnvgM0rF0dEeHL1N9o2TCGHq0bBuS5y0oErnUNich44HQgTkQygb8C1QFU9TXgc5wksAbIAa53KxZjjKnKVJWPftrEY5+k8cDgzlyeksDg7s2Ddnw3rxq6vJztCtzq1vGNMSYcbN61n4enLGfa6m30TGhIcptGQY8h7MpQG2NMpPj4p008PCWVwiLl0fO6cu3JiURHlXYdjbssERhjTIg0qFWdE+Ib8rfhxxEfWztkcVgiMMaYICkoLOKtH9aTX1jEbWd04PROTTmtYxNEgt8KKM4SgTHGBEHa5t08MGkZyzdlc26PFqgqIhLyJACWCIwxxlV5BYW8/P0aXp2+loa1q/OvK3txTvfmVSIBHGSJwBhjXJS+PYfXZqxl6Akt+cu5XWlUp0aoQzqCJQJjjAmwfXkFfJO2hQt6tqJT83p8d/fpJDQO3WBweSwRGGNMAM36ZRsPTl7Opl376d6qPu2b1qvSSQAsERhjTEBk5+Tz1Odp/HdhJm3j6vDhyL60b1ov1GH5xRKBMcZUUmGRctFrP7J++z7+dHo77hjYgZjq0aEOy2+WCIwx5hjt2HeAhrWqEx0l3Hd2J1o1rEX3Vg1CHVaF2eT1xhhTQarKpEWZDHhuOhMWOPNrnd2teVgmAfBSiyBvtzMfQcb8KlV33BgTXjJ35vDQlFRm/ryNE9s0IiUpNtQhVZo3EkHG/N/nJh03NODzfRpjvGHKkkwemZKKAo8N7cbVJ7UhKgRF4gLNG4kgfdbvc5MenO/TEoExpoJi69TkxMRYnr6wO60bVe1LQivCG4kgsT/OFMkKUdUCPt+nMSYy5RcW8casdRQUKncM7MBpHZtwaoe4KlUeIhC8kQgO497UnMaYyJG6KZsHJi1jxebdnH98yypVJC7QvJEI0mdxKAEUFVrXkDHmqHLzC3npu194feY6GtWuwWtX9WJw9xahDstV3kgEif1Bopxxguga1jVkjDmqDVk5vDFrHcN7tuKRc7vSoHb1UIfkOm8kgvgUaNbduXz0ojetNWCMOcy+vAK+WvEbw3u1plPzenx/z+khnTEs2LyRCABq1nd+LAkYY4qZ8fM2Hpq8nM3Z++nRugHtm9bzVBIALyUCY4wpZue+AzzxWRqTF2+iXZM6/O+P4VMkLtAsERhjPOdgkbgNWTncNqA9t53RPqyKxAWaJQJjjGdk7c2jUe0aREcJowZ3plWjWnRrGZ71gQLJis4ZYyKeqvLfhRkMeG464xdsBOCsbs0tCfhYi8AYE9EyduTw0JTlzPplOymJsfRt2zjUIVU53kkEVn3UGM+ZvDiTRz5KRYAnLujOlSkJEVEkLtC8kQis+qgxnhRXtyYpSbE8deFxtGpYK9ThVFneSARWfdQYT8gvLOL1GWspLII/D+rAqR2bcGrHJqEOq8rzRiKw6qPGRLzUTdncN3EZK3/dzbATfi8SZ8rnjURwGKs+akwkyc0v5B/f/sIbs9YRW6cGr199Imd3ax7qsMKKq5ePishgEVktImtEZFQp2xNEZJqILBGRZSIyxJVASqs+aoyJCBt35PDWD+u4uFdrvr3rNEsCx8C1FoGIRAOvAGcCmcACEZmqqmnFdnsE+K+qvioiXYHPgcSAB2PVR42JKHty8/ky9TcuSY6nY7N6TLv39IiaMSzY3OwaSgHWqOo6ABGZAAwDiicCBer7fm8AbHYlEqs+akzEmLZqKw9PWc5vu3PpmdCQ9k3rWRKoJDcTQSsgo9hyJtCnxD6jga9F5HagDjCotCcSkZHASICEhIRji8aqjxoT1nbsO8ATn6YxZckmOjSty8RbTvZskbhAczMRlDZcX3Kk9nLgXVV9XkT6Au+LSHfVg9d6+h6kOhYYC5CcnGyjvcZ4TGGRcvGrP7JxRw53DOzArQPaUbOad4vEBZqbiSATiC+23Joju35uBAYDqOocEYkB4oCtLsZljAkT2/bk0biOUyTuoSFdaNWoFl1a1C//gaZC3LxqaAHQQUSSRKQGMAKYWmKfjcBAABHpAsQA21yMyRgTBlSVDxds5Iznp/Of+U6RuEFdm1kScIlrLQJVLRCR24CvgGjgbVVdISKPAwtVdSpwD/CGiNyF0210napa148xHrYxK4dRk5fx49os+iTF0q99XKhDiniu3lCmqp/jXBJafN2jxX5PA05xMwZjTPiYuCiTv3yUSnSU8NSF3bm8txWJCwYP3llsjKmqmtWvycntGvPkhd1p0cCKxAWLJQJjTMgcKCji1elrKVLlrjM70r9DE/p3sCJxwWaJwBgTEkszdnH/xGWs3rKH4T1bWZG4ELJEYIwJqv0HCnnhm9W89cN6mtaL4c1rkhnUtVmow/I0SwTGmKDK2JnDuB83MCIlgVHndKZ+TPVQh+R5lgiMMa7b7SsSd6mvSNz0+06npc0YVmVYIjDGuOr7VVt4aHIqW/fk0iuhEe2b1rUkUMVYIjDGuCJrbx6Pf5rGxz9tplOzerx29Ym0b1o31GGZUlgiMMYEXGGRcslrc8jYmcNdgzpyy+ntqFHN1XmwTCX4lQh8tYISVHWNy/EYY8LY1j25xNWpSXSU8PC5XWjdqDadmlup6Kqu3BQtIucCy4FvfMsniMgUtwMzxoSPoiLlg3kbOOO5GXzgKxI3sEszSwJhwp8WweM4E8pMA1DVn0SkvatRGWPCRvr2fYyavIy563ZwcrvGnGZ3BocdfxJBvqruKnHHn1UINcbw34UZ/OWjVGpER/HM8OO4rHe83R0chvxJBCtF5FIgSkSSgD8Dc90NywV5u505izPm23SVxgRIq4a1OLVjE54Y1p3mDWJCHY45Rv4M498GnAgUAZOBXJxkED4y5sOWVNi1AcYNdZaNMRWWV1DImG9+5oWvVwNwSvs43rgm2ZJAmPMnEZytqg+oak/fzyjgHLcDC6j0WXBwGuTCA86yMaZClmzcyfn//IEXv/uFTbtysTmkIoc/XUOP4LQEinu4lHVVV2J/QACFqGq+ZWOMP3IOFPD81z/z9uz1NK8fw9vXJXNGZysSF0mOmghE5GycieVbicgLxTbVx+kmClP2LcaYiti0cz/vz93AlX0SeGBwZ+pZkbiIU1aLYCuQijMmsKLY+j3AKDeDCrj0WRxKAEWFzrINGBtzVNn78/li+a+MSEmgQ7N6zLjvdJsxLIIdNRGo6hJgiYh8oKq5QYwp8BL7g0Q54wTRNaxryJgyfL3iNx75KJWsfQdIToylfdO6lgQinD9jBK1E5CmgK3Do0gBV7ehaVIEWnwLNujuXj170prUGjCnF9r15jJ66gk+X/Urn5vV489pkKxLnEf4kgneBJ4HncK4Wup5wHCOoWd/5sSRgzBEKi5SLX/2RzbtyufesjvzxtHZUj7YicV7hTyKorapfichzqroWeERE7PpLYyLAlt25NKnrFIn76/ndaN2oFh2aWX0gr/En5eeJc8/4WhG5WUTOB5q6HJcxxkVFRcr7czcw8PkZfDBvAwADOje1JOBR/rQI7gLqAncATwENgBvcDMoY45512/YyavJy5q/fQb/2cZzeyb7XeV25iUBV5/l+3QNcDSAird0Myhjjjg8XbOTRj1dQs1oUz17cg0tObG1F4kzZiUBEegOtgB9UdbuIdAMeAM4ALBkYE2ZaN6rN6Z2cInFN61t9IOMo687ivwEXAUtxBoin4BSb+z/g5uCEZ4ypjLyCQv75nTOx4L1nd+KU9nGc0j4uxFGZqqasFsEw4HhV3S8iscBm3/Lq4IRmjKmMRRt2cP/EZazdto9Lk1ujqtYNZEpVViLIVdX9AKq6Q0RWWRIwpurbl1fA379azbg56bRsUItxN6RwWkebNcwcXVmJoK2IHKwwKkBisWVUdXh5Ty4ig4EXgWjgTVV9ppR9LgVG4xQDWqqqV/gfvjGmpM279vOf+Ru55qQ23De4M3Vr+nNxoPGyst4hF5VYfrkiTywi0cArwJlAJrBARKaqalqxfToADwKnqOpOEbHr2Iw5Btk5+Xy2/Feu6OMUiZt1/wCa2WCw8VNZRee+q+RzpwBrVHUdgIhMwBl3SCu2zx+AV1R1p++YWyt5TGM858vU3/jLx6ns2HeAPm1jadekriUBUyFuFhNpBWQUW870rSuuI9BRRGaLyFxfV9IRRGSkiCwUkYXbtm1zKVxjwsvWPbn86YNF3PzvRTSpW5OPbz2Fdk2sSJypODc7D0u7PKHkrDDVgA7A6Tj3JcwSke6quuuwB6mOBcYCJCcn28wyxvMKi5RLX5vD5uxc7ju7EyNPbWtF4swx8zsRiEhNVc2rwHNnAvHFllvjXIJacp+5qpoPrBeR1TiJYUEFjmOMZ/yavZ9m9WKcInFDuxHfqLaVijaVVu5XCBFJEZHlwC++5eNF5J9+PPcCoIOIJIlIDWAEMLXEPh8BA3zPG4fTVbSuAvEb4wlFRcq7s9cz8PkZ/PtgkbhOTS0JmIDwp0XwEnAezoc2qrpURAaU9yBVLRCR24CvcC4ffVtVV4jI48BCVZ3q23aWiKQBhcB9qpp1jOdiTERas3UvoyYtY+GGnZzasQlndLaL60xg+ZMIolR1Q4k7Egv9eXJV/Rz4vMS6R4v9rsDdvh9jTAkT5m/k0akrqFU9mucvOZ7hvVrZ3cEm4PxJBBkikgKo796A24Gf3Q3LGAOQ0Lg2g7o05bGh3WlSr2aowzERyp9EcAtO91ACsAX41rfOGBNgufmFvPTdLwDcP7gzJ7eL4+R2ViTOuMufRFCgqiNcj8Rtebudyesz5tu8xaZKWpi+g/snLWPdtn2M6B1vReJM0PiTCBb4Luv8EJisqntcjinwMubDllTQIhg3FK6dasnAVBl78wr4+5ereG/uBlo1rMV7N6RwqhWJM0FU7uWjqtoOeBI4EVguIh+JSHi1ENJnOUkAoPCAs2xMFfFb9n4mLMjg2r6JfHXnqZYETND5dSuiqv6oqncAvYDdwAeuRhVoif1BfKcaXcNZNiaEdu47wPtznfsB2jd1isSNHtqNOlYp1IRAue86EamLUyxuBNAF+Bg42eW4Ais+BZp1d8YILnrTuoVMyKgqX6T+xqMfp7IrJ5+T2zWmXZO6Nm2kCSl/vn6kAp8Az6qq9akYc4y27s7lLx+n8tWKLRzXqgHv3dDHisSZKsGfRNBW9WAHe5iywWITYoVFyiWvz+G37FwePKczN/ZLopoViTNVRFmT1z+vqvcAk0TkiIqf/sxQVmWUNlhsicAEweZd+2le3ykS9/iw7sQ3qkVbawWYKqasFsGHvn8rNDNZlXRwsFiLbLDYBEVhkfLenHSe/XI1Dw7pzDV9E23eYFNllTVD2Xzfr11U9bBk4CsmV9kZzILHBotNEK3Zuof7Jy5j8cZdnN6pCQO7NAt1SMaUyZ9OyhtKWXdjoANxXc360CDekoBx1X/mbWTIiz+wfvs+xlx2PO9c15tWDWuFOixjylTWGMFlOJeMJonI5GKb6gG7Sn+UMd6WGFebs7o1Y/TQbsTVtSJxJjyUNUYwH8jCmVnslWLr9wBL3AzKmHCRm1/ImG9/RhBGnWNF4kx4KmuMYD2wHqfaqDGmhHnrshg1eTnrt+/jyj4JViTOhK2yuoZmqOppIrKTwyedF5w5ZWJdj86YKmhPbj7/9+Uq/j13IwmxtfnPTX04ub21Akz4Kqtr6OB0lPYON6aYLbvzmLgok5v6JXH3WR2pXcPqA5nwVlbX0MG7ieOBzap6QET6AT2Af+MUnzPGE3bsO8BnyzZzdd9E2jety6z7z7AZw0zE8Ofy0Y9wpqlsB7yHU3juP65GZUwVoap8snQzZ74wg8c/TWPdtr0AlgRMRPGnTVukqvkiMhz4h6q+JCJ21ZCJeFt25/LwlFS+XbmFHq0b8MHFfaw8hIlIfk1VKSKXAFcDF/jWVXcvJGNCr7BIudRXJO7hIV24/pREKxJnIpY/ieAG4E84ZajXiUgSMN7dsIwJjcydObRoUIvoKOGJYd1JiK1NYlydUIdljKv8maoyFbgDWCginYEMVX3K9ciMCaLCIuXNWesY9MIM/u2bOezUjk0sCRhP8GeGsv7A+8AmnHsImovI1ao62+3gjAmG1b/t4f5Jy1iasYuBnZtyVjcrEme8xZ+uoTHAEFVNAxCRLjiJIdnNwIwJhn/P3cBjn6ygXkx1XhxxAkOPb2l3BxvP8ScR1DiYBABUdaWI1HAxJmNcd7AcRPumdRlyXAsePa8rja1InPEofxLBYhF5HacVAHAlVnTOhKn9Bwp54ZvVREUJD57ThZPaNuakto1DHZYxIeXP9XA3A2uB+4EHgHXAH90MyhV5uyE7w5m/2HjSnLVZDH5xJm/MWk9OXiGqR8zAaownldkiEJHjgHbAFFV9NjghucAmr/e03bn5/O3zVYyfv5E2jWvznz/0sVLRxhRz1BaBiDyEU17iSuAbESltprLwUNrk9cYztu7O46Mlmxh5alu+/POplgSMKaGsrqErgR6qegnQG7ilok8uIoNFZLWIrBGRUWXsd7GIqIi4cyVSYn+cK1+BqGo2eb0HZO3N493Z6wFo37QuPzwwgIeGdKFWjegQR2ZM1VNW11Cequ4DUNVtIlKh++tFJBpnZrMzgUxggYhMLX4Fkm+/ejg3rM2rUOTHzPqFI5mqMnXpZkZPXcHevAJO7diEtk3q2hVBxpShrETQtthcxQK0Kz53saoOL+e5U4A1qroOQEQmAMOAtBL7PQE8C9xbkcArJH0WhxJAUaGzbGMEEWfzrv088lEq36/aygnxDXn24h5WJM4YP5SVCC4qsfxyBZ+7FZBRbDkT6FN8BxHpCcSr6qcictREICIjgZEACQkJFQwDpytIopxxguga1jUUgQoKixgxdi7b9uTxl/O6ct3JiURH2Y1hxvijrIlpvqvkc5f2v/BQv4yvq2kMcF15T6SqY4GxAMnJyRXv24lPgWbdITcbLnrTWgMRJGNHDi0b1qJadBRPX3gcCbG1SWhcO9RhGRNW3Kyrm4kzu9lBrYHNxZbrAd2B6SKSDpwETHVtwLhmfWgQb0kgQhQUFjF25loGvTCD9+ekA9CvQ5wlAWOOgZuTrS4AOvjKVm8CRgBXHNyoqtkUmw9ZRKYD96rqQhdjMhFg5a+7eWDSMpZlZnNm12acc1yLUIdkTFjzOxGISE1VzfN3f1UtEJHbgK+AaOBtVV0hIo8DC1V1asXDNV73/px0HvskjQa1qvPyFT0597gWViTOmErypwx1CvAW0ABIEJHjgZtU9fbyHquqnwOfl1j36FH2Pd2fgI03HSwS17FZPc4/viV/Oa8rsXWs9qExgeBPi+Al4Dycu4xR1aUiMsDVqIzxyTlQwHNf/Uy1aOGhIV3o07YxfaxInDEB5c9gcZSqbiixrtCNYIwpbvaa7Zz9j5m8PXs9BwqKrEicMS7xp0WQ4eseUt/dwrcDP7sblvGy7P35PP3ZSj5cmEFSXB3++8e+pCTFhjosYyKWP4ngFpzuoQRgC/Atx1B3yBh/bd+bxyfLNnPzae24c1AHYqpbfSBj3FRuIlDVrTiXfhrjmm178vhk6WZu6JdEuyZ1+eGBM2ww2Jgg8eeqoTcopVKbqo50JSLjKarKRz9t4rFP0sjJK2RA56YkxdWxJGBMEPnTNfRtsd9jgAs5vIaQMcdk0679PDxlOdNXb6NXglMkLimuTqjDMsZz/Oka+rD4soi8D3zjWkRuydvt1BrKmG9lJqoAp0jcHLL2HmD0+V25uq8ViTMmVI6lxEQS0CbQgbjKpqqsMjZm5dCqkVMk7pnhPUiIrU18rNUHMiaUyr2PQER2isgO388unNbAQ+6HFkA2VWXIFRQW8er0tQwaM4P35qQDcEr7OEsCxlQB5U1eL8DxOEXjAIo0HO/qsfkIQmrF5mwemLSM1E27ObtbM861InHGVCllJgJVVRGZoqonBisgV8SnQKMkyMmCQY9Zt1AQjfsxnSc+TaNh7Rq8emUvqxRqTBXkzxjBfBHppaqLXY/GLRnzYed6p0Xw5Sho1tWSgcsOFonr3Lwew05oxV/O60LD2nZJqDFV0VETgYhUU9UCoB/wBxFZC+zDmXlMVbVXkGKsvNLGCCwRuGJfXgF//2o11aOFh8/takXijAkDZbUI5gO9gAuCFIt7bIwgKGb+vI0HJy9nc/Z+ru2beKhVYIyp2spKBAKgqmuDFIt7bM5iV2Xn5PPEZ2lMXJRJ2yZOkbjeiVYkzphwUVYiaCIidx9to6q+4EI87qlZ3/mxJBBw2/fl8cXyX/nT6e24Y6AViTMm3JSVCKKBuvhaBsYUt3VPLlN/2sxN/dseKhLXyOoDGROWykoEv6rq40GLxIQFVWXS4k088Wka+/MLGdilGUlxdSwJGBPGyh0jiBhWa6jSMnbk8NCU5cz6ZTvJbRrxzEVWJM6YSFBWIhgYtCjcZrWGKq2gsIjL35jLzn0HeGJYN67s04YoKxJnTEQ4aiJQ1R3BDMRVdh/BMUvfvo/42NpUi47i2YudInGtG1l9IGMiiT+T14e/xP4c6umKqmb3Efghv7CIV6at4awxMw8ViTu5XZwlAWMi0LGUoQ5z4VczL9hSN2Vz/8RlpP26m3OPa8F5PVqGOiRjjIu8kQjSZ3EoARQVWtdQGd6ZvZ4nP1tJbJ0avHbViQzu3jzUIRljXOaNRGAlJsp1sBxEt5YNGN6zFY+c25UGtauHOixjTBB4IxFYiYmj2ptXwLNfrqJGdBSPnNeVlKRYUpKsPIQxXuKNwWJwyks0iLckUMz01Vs5e8xM3p+7AcVpFRhjvMcbLQKwG8qK2bnvAE98lsbkxZto37QuE28+mRPbNAp1WMaYEPFGi+DgDWW7Njg3lGXMD3VEIbUz5wBfr9jCHWe057M7+lkSMMbjXE0EIjJYRFaLyBoRGVXK9rtFJE1ElonIdyLSxpVAbPJ6tu7OZezMtagqbZvUZfYDZ3D3WZ2oWc0qhRrjda4lAhGJBl4BzgG6ApeLSNcSuy0BklW1BzAReNaVYA5eNQSeu2pIVfnvggwGvjCD57/+mfSsHAC7IsgYc4ibYwQpwBpVXQcgIhOAYUDawR1UdVqx/ecCV7kSiUevGsrYkcODk5fzw5rtpCTF8szw46xInDHmCG4mglZARrHlTKBPGfvfCHxR2gYRGQmMBEhISDi2aDw2Mc3BInG7cvJ58oLuXJGSYEXijDGlcjMRlPapU+r1iSJyFZAMnFbadlUdC4wFSE5OPrZrHD1y1dD67ftI8BWJ+/vFx9OmcW1aNqwV6rCMMVWYm4PFmUB8seXWwOaSO4nIIOBhYKiq5rkSiQeuGsovLOKf3/3C2WNmMu7HdAD6tmtsScAYUy43WwQLgA4ikgRsAkYAVxTfQUR6Aq8Dg1V1q2uRRHgZ6mWZu7h/4jJW/baH849vydATrEicMcZ/riUCVS0QkduAr3DmP35bVVeIyOPAQlWdCvwdZ17k/4kIwEZVHRrwYCK41tDbP6znyc/SaFKvJm9ck8yZXZuFOiRjTJhx9c5iVf0c+LzEukeL/T7IzeMfEp8CjZIgJwsGPRYRrYGDReJ6tG7AZb3jGXVOFxrUsktCjTEV540SExnzYed6p0Xw5Sho1jVsk8Ge3Hye+WIVNatF8+j5XUlOjCU50YrEGWOOnTdKTETIncXTVm3lrDEzGT9/I9WixYrEGWMCwhstgkNTVWpYTlW5Y98BHv9kBR/9tJmOzeryrytPpmeC1QcyxgSGNxLBYcLvW3T2/ny+W7mVPw/swK0D2lOjmjcacsaY4PDGJ0ppU1VWcb9l5/LaDKdIXFJcHX4YdQZ3ndnRkoAxJuC80SIIo8tHVZUJCzJ4+rOV5BcVMbhbcxLj6tgVQcYY13gjEYRJ0bkNWfsYNWk5c9ZlcVLbWJ4Z3oNEK1pMdnAAABFVSURBVBJnzGHy8/PJzMwkNzc31KFUSTExMbRu3Zrq1f3/8uiNRABVvuhcQWERV7wxj+z9+Tx94XGM6B1vReKMKUVmZib16tUjMTER342oxkdVycrKIjMzk6SkJL8f551EUEWt3baXNr4icc9f6hSJa9HA6gMZczS5ubmWBI5CRGjcuDHbtm2r0ONs5DFEDhQU8Y9vf2bwP2by3pwNAJzUtrElAWP8YEng6I7ltbEWQQj8lLGLByYuY/WWPQw7oSUX9GwV6pCMMR7mnRZB3m7Izgh5Ceq3fljP8H/NJnt/Pm9dm8yLI3oSW6dGSGMyxlSMiHDPPfccWn7uuecYPXq034/fsmUL5513Hscffzxdu3ZlyJAhAEyfPp3zzjvviP2nTp3KM888A8Do0aN57rnnALjuuuuYOHFiJc7E4Y1EUAXmIzhYDuKE+AaMSEng67tPZWAXqxRqTDiqWbMmkydPZvv27cf0+EcffZQzzzyTpUuXkpaWduhD/miGDh3KqFGjjulY/vBG11AI5yPYnZvP3z5fRUz1KP56fjdObBPLiW2sSJwxgXLZ63OOWHdejxZc3TeR/QcKue6dI7/4XXxiay5JjmfHvgPc8u9Fh2378I99yz1mtWrVGDlyJGPGjOGpp546bNuGDRu44YYb2LZtG02aNOGdd945YordX3/9lbPOOuvQco8ePY44xoIFCxg5ciSTJk1i5syZLFy4kJdffrnc2I6FN1oEB28og6DeUPZt2hbOfGEGHy7YSI1qUVYkzpgIcuutt/LBBx+QnZ192PrbbruNa665hmXLlnHllVdyxx13lPrYG2+8kQEDBvDUU0+xefPhkzf++OOP3HzzzXz88ce0bdvW1fMAr7QIgnxDWdbePB77JI2pSzfTuXk9xl6dzPHxDV09pjFeVdY3+Fo1osvcHlunhl8tgNLUr1+fa665hpdeeolatX6/2m/OnDlMnjwZgKuvvpr777//iMeeffbZrFu3ji+//JIvvviCnj17kpqaCsDKlSsZOXIkX3/9NS1bBme2QW+0CMC5maxBfFC6hPbkFjBt9VbuGtSRqbf1syRgTIS68847eeutt9i3b99R9zna5ZyxsbFcccUVvP/++/Tu3ZuZM2cC0KJFC2JiYliyZIkrMZfGO4nAZZt37eeVaWtQVRLj6jB71Bn8eVAHKxJnTASLjY3l0ksv5a233jq07uSTT2bChAkAfPDBB/Tr1++Ix33//ffk5OQAsGfPHtauXXtoHKFhw4Z89tlnPPTQQ0yfPt39k8ASQaUVFSn/nruBs8bM5OXv17Ahy/nj1o+xInHGeME999xz2NVDL730Eu+88w49evTg/fff58UXXzziMYsWLSI5OZkePXrQt29fbrrpJnr37n1oe7Nmzfjkk0+49dZbmTdvnuvnIOE2gJmcnKwLFy6s+ANf6x/wMYL12/cxatIy5q3fwSntG/O3C3uQ0Lh2QJ7bGFO6lStX0qVLl1CHUaWV9hqJyCJVTS5tf28MFh+8j0CLnPsIrp1a6WRQUFjEVW/OY3duPs9e1INLklvbbe/GmLDkjUQQwPsI1mzdQ2LjOlSLjmLMZSfQpnFtmtWPCWCwxhgTXN4YIwjAfQR5BYW88M3PDP7HLMb5isSlJMVaEjDGhD1vtAgqeR/B4o07eWDiMn7ZupfhPVsx3IrEGWMiiDcSARzzxDRvzFzH01+spEX9GN65vjcDOjV1KUBjjAkN7ySCCioqUqKihF5tGnJlnwQeGNyZenZJqDEmAnljjKACsvfnc//EpTz2yQoATmwTy5MXHGdJwBhzmClTpiAirFq1CoD09HRq1apFz5496dKlCykpKYwbN+6Ixw0bNoy+fY+trIVbLBEU89WK3zjzhRlMWryJOjWrWZE4YyJFxnyY9XxAS9CPHz+efv36HbqLGKBdu3YsWbKElStXMmHCBMaMGcM777xzaPuuXbtYvHgxu3btYv369QGLpbKsawjYvjePv368gs+W/0rXFvV5+7redG/VINRhGWPK88Uo+G152fvk7f79PiKJci4cqVn/6Ps3Pw7OKXt+gL179zJ79mymTZvG0KFDS52Upm3btrzwwgvcc889XH/99QBMmjSJ888/n2bNmjFhwgQefPDB8s4wKLzTIihjhrK9uQXM+mUb953diY9vO8WSgDGRJDf79/uItMhZrqSPPvqIwYMH07FjR2JjY1m8eHGp+/Xq1etQ1xE4rYjLL7+cyy+/nPHjx1c6jkDxRouglDuLN9U7jimLM7l1QHsS4+rw44MDqVvTGy+HMRGjnG/ugPP/f9xQ52bS6BoBKTMzfvx47rzzTgBGjBjB+PHjufXWW4/Yr3j38pYtW1izZg39+vVDRKhWrRqpqal07969UrEEgquffCIyGHgRiAbeVNVnSmyvCbwHnAhkAZepanrAAyl2Z7EWHuCnmZ9w1eodFCmc16MliXF1LAkYE6niU5yyMumznJtJK5kEsrKy+P7770lNTUVEKCwsRET405/+dMS+S5YsOVTz58MPP2Tnzp0kJSUBsHv3biZMmMCTTz5ZqXgCwbWuIRGJBl4BzgG6ApeLSNcSu90I7FTV9sAY4P9cCSaxPyAokK9RPJEaS682jfj6rlNJjKvjyiGNMVVIfAr0vycgBScnTpzINddcw4YNG0hPTycjI4OkpCQyMzMP2y89PZ17772X22+/HXBaEV9++SXp6emkp6ezaNGiwwaaQ8nNr8EpwBpVXQcgIhOAYUBasX2GAaN9v08EXhYRURcu19FD/yq3ntGeMwalWJE4Y0yFjR8//oiJ5C+66CKefvpp1q5dS8+ePcnNzaVevXrcfvvtXH/99aSnp7Nx40ZOOumkQ49JSkqifv36zJs3jz59+gT7NA7jZiJoBWQUW84ESp7toX1UtUBEsoHGwPbiO4nISGAkcMQk0H5Jn8XBj/waogyM+RksCRhjjkFpk8Xccccdpc5NfFBiYiKbNm06Yv3RBpmDzc2rhkr7pC35Td+ffVDVsaqarKrJTZo0qXgkif2hWgxINBLEyeuNMSYcuNkiyATiiy23BjYfZZ9MEakGNAB2BDySAA8WGWNMJHEzESwAOohIErAJGAFcUWKfqcC1wBzgYuB7N8YHAOfD3xKAMRFBVW2M7yiO5SPUta4hVS0AbgO+AlYC/1XVFSLyuIgM9e32FtBYRNYAdwOjSn82Y4xxxMTEkJWVZSVgSqGqZGVlERNTsXlSvDNnsTEmIuTn55OZmUlubm6oQ6mSYmJiaN26NdWrH14o0+YsNsZEjOrVqx+6KcsEhndqDRljjCmVJQJjjPE4SwTGGONxYTdYLCLbgA3H+PA4Sty17AF2zt5g5+wNlTnnNqpa6h25YZcIKkNEFh5t1DxS2Tl7g52zN7h1ztY1ZIwxHmeJwBhjPM5riWBsqAMIATtnb7Bz9gZXztlTYwTGGGOO5LUWgTHGmBIsERhjjMdFZCIQkcEislpE1ojIERVNRaSmiHzo2z5PRBKDH2Vg+XHOd4tImogsE5HvRKRNKOIMpPLOudh+F4uIikjYX2rozzmLyKW+v/UKEflPsGMMND/e2wkiMk1Elvje30NCEWegiMjbIrJVRFKPsl1E5CXf67FMRHpV+qCqGlE/QDSwFmgL1ACWAl1L7PMn4DXf7yOAD0MddxDOeQBQ2/f7LV44Z99+9YCZwFwgOdRxB+Hv3AFYAjTyLTcNddxBOOexwC2+37sC6aGOu5LnfCrQC0g9yvYhwBc4MzyeBMyr7DEjsUWQAqxR1XWqegCYAAwrsc8wYJzv94nAQAnvWS7KPWdVnaaqOb7FuTgzxoUzf/7OAE8AzwKRULPYn3P+A/CKqu4EUNWtQY4x0Pw5ZwXq+35vwJEzIYYVVZ1J2TM1DgPeU8dcoKGItKjMMSMxEbQCMootZ/rWlbqPOhPoZAONgxKdO/w55+JuxPlGEc7KPWcR6QnEq+qnwQzMRf78nTsCHUVktojMFZHBQYvOHf6c82jgKhHJBD4Hbg9OaCFT0f/v5YrE+QhK+2Zf8hpZf/YJJ36fj4hcBSQDp7kakfvKPGcRiQLGANcFK6Ag8OfvXA2ne+h0nFbfLBHprqq7XI7NLf6c8+XAu6r6vIj0Bd73nXOR++GFRMA/vyKxRZAJxBdbbs2RTcVD+4hINZzmZFlNsarOn3NGRAYBDwNDVTUvSLG5pbxzrgd0B6aLSDpOX+rUMB8w9ve9/bGq5qvqemA1TmIIV/6c843AfwFUdQ4Qg1OcLVL59f+9IiIxESwAOohIkojUwBkMnlpin6nAtb7fLwa+V98oTJgq95x93SSv4ySBcO83hnLOWVWzVTVOVRNVNRFnXGSoqobzPKf+vLc/wrkwABGJw+kqWhfUKAPLn3PeCAwEEJEuOIlgW1CjDK6pwDW+q4dOArJV9dfKPGHEdQ2paoGI3AZ8hXPFwduqukJEHgcWqupU4C2c5uManJbAiNBFXHl+nvPfgbrA/3zj4htVdWjIgq4kP885ovh5zl8BZ4lIGlAI3KeqWaGLunL8POd7gDdE5C6cLpLrwvmLnYiMx+nai/ONe/wVqA6gqq/hjIMMAdYAOcD1lT5mGL9exhhjAiASu4aMMcZUgCUCY4zxOEsExhjjcZYIjDHG4ywRGGOMx1kiMFWOiBSKyE/FfhLL2DfxaFUaK3jM6b4Kl0t95Rk6HcNz3Cwi1/h+v05EWhbb9qaIdA1wnAtE5AQ/HnOniNSu7LFN5LJEYKqi/ap6QrGf9CAd90pVPR6nIOHfK/pgVX1NVd/zLV4HtCy27SZVTQtIlL/H+S/8i/NOwBKBOSpLBCYs+L75zxKRxb6fk0vZp5uIzPe1IpaJSAff+quKrX9dRKLLOdxMoL3vsQN9de6X++rE1/Stf0Z+n9/hOd+60SJyr4hcjFPP6QPfMWv5vskni8gtIvJssZivE5F/HmOccyhWbExEXhWRheLMQ/CYb90dOAlpmohM8607S0Tm+F7H/4lI3XKOYyKcJQJTFdUq1i00xbduK3CmqvYCLgNeKuVxNwMvquoJOB/Emb6SA5cBp/jWFwJXlnP884HlIhIDvAtcpqrH4dyJf4uIxAIXAt1UtQfwZPEHq+pEYCHON/cTVHV/sc0TgeHFli8DPjzGOAfjlJQ46GFVTQZ6AKeJSA9VfQmnDs0AVR3gKzvxCDDI91ouBO4u5zgmwkVciQkTEfb7PgyLqw687OsTL8SpoVPSHOBhEWkNTFbVX0RkIHAisMBXWqMWTlIpzQcish9Ixyll3AlYr6o/+7aPA24FXsaZ3+BNEfkM8LvMtapuE5F1vhoxv/iOMdv3vBWJsw5OyYXis1NdKiIjcf5ft8CZpGVZicee5Fs/23ecGjivm/EwSwQmXNwFbAGOx2nJHjHRjKr+R0TmAecCX4nITTgle8ep6oN+HOPK4kXpRKTUOSp89W9ScAqdjQBuA86owLl8CFwKrAKmqKqK86nsd5w4M3U9A7wCDBeRJOBeoLeq7hSRd3GKr5UkwDeqenkF4jURzrqGTLhoAPzqqzF/Nc634cOISFtgna87ZCpOF8l3wMUi0tS3T6z4P1/zKiBRRNr7lq8GZvj61Buo6uc4A7GlXbmzB6cUdmkmAxfg1NH/0LeuQnGqaj5OF89Jvm6l+sA+IFtEmgHnHCWWucApB89JRGqLSGmtK+MhlghMuPgXcK2IzMXpFtpXyj6XAaki8hPQGWc6vzScD8yvRWQZ8A1Ot0m5VDUXp7Lj/0RkOVAEvIbzofqp7/lm4LRWSnoXeO3gYHGJ590JpAFtVHW+b12F4/SNPTwP3KuqS3HmKl4BvI3T3XTQWOALEZmmqttwrmga7zvOXJzXyniYVR81xhiPsxaBMcZ4nCUCY4zxOEsExhjjcZYIjDHG4ywRGGOMx1kiMMYYj7NEYIwxHvf/J5NNU5n9ydkAAAAASUVORK5CYII=\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "from sklearn.metrics import roc_curve\n",
    "from sklearn.metrics import roc_auc_score\n",
    "from matplotlib import pyplot\n",
    "\n",
    "lr_probs = ada.predict_proba(X_test)\n",
    "ns_probs = [0 for _ in range(len(y_test))]\n",
    "lr_probs = lr_probs[:, 1]\n",
    "\n",
    "# calculate scores\n",
    "ns_auc = roc_auc_score(y_test, ns_probs)\n",
    "lr_auc = roc_auc_score(y_test, lr_probs)\n",
    "\n",
    "# summarize scores\n",
    "print('No Skill: ROC AUC=%.3f' % (ns_auc))\n",
    "print('ADA: ROC AUC=%.3f' % (lr_auc))\n",
    "\n",
    "# calculate roc curves\n",
    "ns_fpr, ns_tpr, _ = roc_curve(y_test, ns_probs)\n",
    "lr_fpr, lr_tpr, _ = roc_curve(y_test, lr_probs)\n",
    "\n",
    "# plot the roc curve for the model\n",
    "pyplot.plot(ns_fpr, ns_tpr, linestyle='--', label='No Skill')\n",
    "pyplot.plot(lr_fpr, lr_tpr, marker='.', label='ADA')\n",
    "\n",
    "# axis labels\n",
    "pyplot.xlabel('False Positive Rate')\n",
    "pyplot.ylabel('True Positive Rate')\n",
    "\n",
    "# show the legend\n",
    "pyplot.legend()\n",
    "\n",
    "# show the plot\n",
    "pyplot.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Training the SVM model"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.svm import SVC\n",
    "from sklearn.metrics import classification_report,confusion_matrix,accuracy_score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [],
   "source": [
    "model_svm = SVC()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\POOJA\\AppData\\Local\\Continuum\\anaconda3\\lib\\site-packages\\sklearn\\svm\\base.py:193: FutureWarning: The default value of gamma will change from 'auto' to 'scale' in version 0.22 to account better for unscaled features. Set gamma explicitly to 'auto' or 'scale' to avoid this warning.\n",
      "  \"avoid this warning.\", FutureWarning)\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "SVC(C=1.0, cache_size=200, class_weight=None, coef0=0.0,\n",
       "    decision_function_shape='ovr', degree=3, gamma='auto_deprecated',\n",
       "    kernel='rbf', max_iter=-1, probability=False, random_state=None,\n",
       "    shrinking=True, tol=0.001, verbose=False)"
      ]
     },
     "execution_count": 53,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model_svm.fit(X_train, y_train)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Predictions and Evaluation"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "metadata": {},
   "outputs": [],
   "source": [
    "predictions_svm = model_svm.predict(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Overall accuracy of SVM model using test-set is : 96.682464\n"
     ]
    }
   ],
   "source": [
    "acc_svm = accuracy_score(y_true=y_test, y_pred= predictions_svm)\n",
    "print(\"Overall accuracy of SVM model using test-set is : %f\" %(acc_svm*100))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              precision    recall  f1-score   support\n",
      "\n",
      "           0       0.97      0.94      0.95        78\n",
      "           1       0.96      0.98      0.97       133\n",
      "\n",
      "    accuracy                           0.97       211\n",
      "   macro avg       0.97      0.96      0.96       211\n",
      "weighted avg       0.97      0.97      0.97       211\n",
      "\n"
     ]
    }
   ],
   "source": [
    "print(classification_report(y_test,predictions_svm))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 57,
   "metadata": {
    "scrolled": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[[ 73   5]\n",
      " [  2 131]]\n"
     ]
    }
   ],
   "source": [
    "print(confusion_matrix(y_test,predictions_svm))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Model Accuracy plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 58,
   "metadata": {},
   "outputs": [],
   "source": [
    "n_groups = 3\n",
    "ind = np.arange(n_groups)\n",
    "algo = ('RF','ADA','SVM')\n",
    "accuracy = (acc_rf, acc_ada,acc_svm)\n",
    "loss = (1-acc_rf, 1-acc_ada, 1-acc_svm)\n",
    "precision = ()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 59,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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JElSYwx4kiRJjXGIVpIkqTH24EmSJDXGgCdJktQYA54kSVJjxv2NjrfddtvabbfBj6WUJElq109/+tPlVbXturaP+4C32267sXDhwrEuQ5IkadQkuW992x2ilSRJaowBT5IkqTHjfohWkiSNndWrV+M9dTe/JGy11cj74Qx4kiRp2JYvX86CBQtYsWLFWJfSrK233pq99tqLbbbZZtj7GvAkSdKwLViwgJ122onJkyeTZKzLaU5Vcf/997NgwQL23XffYe9vwJMkScOyevVqVqxYweTJk5k40SjRL5MnT+aBBx5g9erVwx6udZKFJEkaljXX3Nlz119rvt+RXONowJMkSWqM/aqSJGmz2KNPx13Up+O2zB48SZKkEVi5cuVYl7BOBjxJktSEE044gZkzZ3LggQdy7LHHsmTJEgA+8YlPMGPGDA466CBmzpzJ/PnzAbjiiit4znOew0EHHcSMGTP45je/CXSufVu6dOna4+66665r95k2bRrvfe97OeKIIzjxxBO59957OeKIIzj44IN5xjOewamnnrr2mrnly5fzjne8gwMOOICDDjqIl7zkJQAccMAB3HTTTWuPf/755/PKV75ys34XDtFKkqQmnHPOOey6664AfOADH+Dd7343s2bN4r3vfS/XX389U6dO5ZFHHgFg3rx5zJ49m+uuu47p06ezYsWKtds2ZMGCBVx77bUk4dFHH+Xyyy9n0qRJrFq1ipe//OVcdtllzJo1i/e///3cfffdfPvb32bbbbflvvs6j4899dRTOffcczn00EMBOPfcczn33HM363dhwJMkSU245JJL+PSnP82yZcv49a9/ze67787222/P6173OqZOnQrADjvsAMDVV1/NMcccw/Tp04HOTYV33nnnjTrPG97whrUzXFevXs0ZZ5zBDTfcQFWxZMkSZsyYwaxZs/jP//xP/v7v/55tt90WgN122w3o9DT+1V/9FUuWLOGOO+4gCc9//vM363fR9yHaJB9KMj9JJXnmetqdleTu7uvsftclSZLaccMNN/DhD3+Yq666ittuu405c+bw6KOPjuhYEyZMYNWqVWuXBx9n0qRJa9/PmTOH+++/n29+85t873vf49WvfvUGz7v99ttz4okn8rGPfYwPf/jDvPWtbx1RneszGtfgfQ54HnDPuhokeQFwPHAgsD9wdJKjRqE2SZLUgF/84hc84QlP4ElPehLLly/n/PPPB+ClL30pn/rUp7j33nsBeOSRR3jkkUc46qijuOqqq5g3bx4AK1as4KGHHgJgn332WXs93uc//3kefvjh9Z539913Z7vttmPx4sVceumla7e97GUv45xzzmHZsmUAa4doAU455RTOO+88vv71r/Oa17xmM34THX0PeFV1XVUt3ECzVwIXVdXDVbUM+DidwCdJkrRBRx99NPvuuy/77bcfRx11FDNmzADgBS94AWeddRYvfvGLOeigg3jhC1/Ifffdx7777suFF17I8ccfz4EHHsghhxzCnXfeCXSu5TvllFM4/PDDueWWW5g8efI6z3vqqady4403MmPGDN74xjdy5JFHrt12xhlnsM8++/CsZz2LGTNmcOKJJ67dNjAwwIwZM3jta1+7dth4c8pI7o48ohMl84Fjq+r2IbZdDny6qj7bXT4G+LOq+t0NHXdgYKAWLtxQfpQkSZvLqlWrmDdvHtOnT2fChAljXc64tHTpUvbbbz+uv/569t577yHbrO97TvLTqhpY1/G3pEkWvUlznc8+SXI6cPqa5Y29IFLSlq9fN0ntF2++KmkkPvKRj/Ce97yHt7zlLesMd5tqSwl4C4BpPcu/1V33G6pqDjBnzfLAwMDodEFKkiRtBieffDInn3xyX8+xpdzo+FLgxCQ7JtkWeCPwmTGuSZIkaVwajduknJtkITAAXJPkru76K5PMBKiqrwGfBW4D7gC+XFX/1e/aJEmSWtT3IdqqOgU4ZYj1xwxafjfw7n7XI0mS1LotZYhWkiRJm8mWMslCkiSNd3v0aS78IuesD5c9eJIk6XFj5cqVj1levXo1q1evHvH+Wyp78CRJUhO+9a1vccYZZ/DLX/6S1atX85d/+ZccfPDBzJw5k1NPPZWrr76aV7ziFTz00EPcfffdPPzww9x1111cddVV/OxnP+Ntb3sbDz/8MNtttx3/8A//wOGHH878+fN/Y//TTjttrD/qBhnwJEnSuPfggw9y0kknccUVVzB16lR+/vOfc/DBB/Nv//Zv3H///ey77768853vBOBd73oXX/3qV7nllluYMmUKy5cv59BDD+WjH/0oRx11FDfccAOzZs3irrvuAviN/ccDA54kSRr3brzxRn784x9z9NFHr11XVSxbtoztttuO449/7CPujz32WKZMmQLAnXfeyTbb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\n",
      "text/plain": [
       "<Figure size 640x480 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "fig, ax = plt.subplots(figsize=(8,6), dpi=80)\n",
    "bar_width = 0.2\n",
    "opacity = 0.9\n",
    "\n",
    "p1 = plt.bar(ind, accuracy , bar_width, alpha=opacity, color='cyan', label='accuracy')\n",
    "p2 = plt.bar(ind+bar_width, loss , bar_width, alpha=opacity, color='red', label='error')\n",
    "plt.title('Comparison Graph')\n",
    "plt.xticks(ind+bar_width/2,algo)\n",
    "plt.xlabel('Algorithm')\n",
    "plt.ylabel('Scores')\n",
    "plt.legend()\n",
    "\n",
    "plt.tight_layout()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Testing"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Variable in Dataset Corresponding Q-chat-10-Toddler Features "
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "A1 Does your child look at you when you call his/her name? \n",
    "A2 How easy is it for you to get eye contact with your child? \n",
    "A3 Doesyourchildpointtoindicatethats/hewantssomething?(e.g.atoythatis outofreach) \n",
    "A4 Doesyourchildpointtoshareinterestwithyou?(e.g.poin9ngatan interes9ngsight) \n",
    "A5 Doesyourchildpretend?(e.g.carefordolls,talkonatoyphone) \n",
    "A6 Doesyourchildfollowwhereyou’relooking? \n",
    "A7 Ifyouorsomeoneelseinthefamilyisvisiblyupset,doesyourchildshowsigns ofwan9ngtocomfortthem?(e.g.strokinghair,huggingthem) \n",
    "A8 Wouldyoudescribeyourchild’sfirstwordsas: \n",
    "A9 Doesyourchildusesimplegestures?(e.g.wavegoodbye) \n",
    "A10 Doesyourchildstareatnothingwithnoapparentpurpose?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 60,
   "metadata": {},
   "outputs": [],
   "source": [
    "l=[[0,1,0,1,0,1,0,1,0,0,15,0,1,1,1]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 61,
   "metadata": {},
   "outputs": [],
   "source": [
    "predict = rfc.predict(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result:\n"
     ]
    },
    {
     "data": {
      "image/jpeg": "/9j/4AAQSkZJRgABAQEAYABgAAD/4RDcRXhpZgAATU0AKgAAAAgABAE7AAIAAAAGAAAISodpAAQAAAABAAAIUJydAAEAAAAMAAAQyOocAAcAAAgMAAAAPgAAAAAc6gAAAAgAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGN2c3JhAAAFkAMAAgAAABQAABCekAQAAgAAABQAABCykpEAAgAAAAM1NAAAkpIAAgAAAAM1NAAA6hwABwAACAwAAAiSAAAAABzqAAAACAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAMjAyMDowNDoyMSAxNTo0NDowMgAyMDIwOjA0OjIxIDE1OjQ0OjAyAAAAYwB2AHMAcgBhAAAA/+ELGGh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC8APD94cGFja2V0IGJlZ2luPSfvu78nIGlkPSdXNU0wTXBDZWhpSHpyZVN6TlRjemtjOWQnPz4NCjx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iPjxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+PHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9InV1aWQ6ZmFmNWJkZDUtYmEzZC0xMWRhLWFkMzEtZDMzZDc1MTgyZjFiIiB4bWxuczpkYz0iaHR0cDovL3B1cmwub3JnL2RjL2VsZW1lbnRzLzEuMS8iLz48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyI+PHhtcDpDcmVhdGVEYXRlPjIwMjAtMDQtMjFUMTU6NDQ6MDIuNTQ0PC94bXA6Q3JlYXRlRGF0ZT48L3JkZjpEZXNjcmlwdGlvbj48cmRmOkRlc2NyaXB0aW9uIHJkZjphYm91dD0idXVpZDpmYWY1YmRkNS1iYTNkLTExZGEtYWQzMS1kMzNkNzUxODJmMWIiIHhtbG5zOmRjPSJodHRwOi8vcHVybC5vcmcvZGMvZWxlbWVudHMvMS4xLyI+PGRjOmNyZWF0b3I+PHJkZjpTZXEgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj48cmRmOmxpPmN2c3JhPC9yZGY6bGk+PC9yZGY6U2VxPg0KCQkJPC9kYzpjcmVhdG9yPjwvcmRmOkRlc2NyaXB0aW9uPjwvcmRmOlJERj48L3g6eG1wbWV0YT4NCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgICAgICAgICAgICAgPD94cGFja2V0IGVuZD0ndyc/Pv/bAEMABwUFBgUEBwYFBggHBwgKEQsKCQkKFQ8QDBEYFRoZGBUYFxseJyEbHSUdFxgiLiIlKCkrLCsaIC8zLyoyJyorKv/bAEMBBwgICgkKFAsLFCocGBwqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKioqKv/AABEIAJwB+AMBIgACEQEDEQH/xAAfAAABBQEBAQEBAQAAAAAAAAAAAQIDBAUGBwgJCgv/xAC1EAACAQMDAgQDBQUEBAAAAX0BAgMABBEFEiExQQYTUWEHInEUMoGRoQgjQrHBFVLR8CQzYnKCCQoWFxgZGiUmJygpKjQ1Njc4OTpDREVGR0hJSlNUVVZXWFlaY2RlZmdoaWpzdHV2d3h5eoOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4eLj5OXm5+jp6vHy8/T19vf4+fr/xAAfAQADAQEBAQEBAQEBAAAAAAAAAQIDBAUGBwgJCgv/xAC1EQACAQIEBAMEBwUEBAABAncAAQIDEQQFITEGEkFRB2FxEyIygQgUQpGhscEJIzNS8BVictEKFiQ04SXxFxgZGiYnKCkqNTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqCg4SFhoeIiYqSk5SVlpeYmZqio6Slpqeoqaqys7S1tre4ubrCw8TFxsfIycrS09TV1tfY2dri4+Tl5ufo6ery8/T19vf4+fr/2gAMAwEAAhEDEQA/APpGiisDxHq0+malpCx3CwQTzlZywXBUbepPTqaxr1o0KftJ7afi7HPicRDDUnVnsrfi0v1N+iuam8Qb/F1pbWV7FPZNbu8qwlXywDHqOQeBxmrY8VWJ0NNV8q48h5fKC7V3A5x0zjH41hHHUJOXvbX/AAtd+mqOeGZYaTl71uW/4Wu15ao2qKxp/E1rBrMmmC3u5biNkDeVEGGGAOevQZGaZb+LLK6upYIba8YwlxI4iyqbQTyQe+Diq+uYfm5edXvb5lf2hhVLk51e9vmt0blFYdt4qtbm8S2azvreSVS0Pnw7BLgZwvNO/wCEqsP7DTVAk5jeXyREFHmb89MZx79aFjMO1dTXX8Lf5oFmGFkm1NaX/C1/zX3m1RWBZXM7+OtSt3mkaFLeMpGWO1SQOQOlHg+5nutLuXuZpJmF3IoaRixA4457VNPFxnUULbuS/wDAXYmnjo1KippbuS/8BdvxN+iiiu09AKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigArA8R6TPqepaQ0dus8EE5acMVwFO3qD16Gt+isa9GNen7Oe2n4O5z4nDwxNJ0p7O34NP9Dm5fD/l+L7S5srKKGxW3dJTEFQbiGHQcnqOaxP7C19dBXRxYRGOG48wTCdcyDPYZ47nmu/orhqZXRnezavfa3W11ttojzquTYepzWbje97W+1a62291GJYafcw+LtVvZYttvcJEIn3A7sKAeOo6d6q6VpOo22havb4+zXNzcSvC24HggAHI6d/cV0tFb/U6ad7v7X/k2/wDwDpWX0k73e8n/AOBu7/4BwWk+G9Rt9Y0y4fShbCBj9om+0iQynH3sZ4+gpYdKY+P3sEYNZQzfbig6KxAwPzI/Cu8qKO1t4p5JooI0lk+/IqAM/wBT3rjWU0oqMYPRSTe3a1tEt7K556yOjCMIweikpO9uitbRJa2VzOt7W4TxTd3L2caQPCqrchyWcjHBG7A79hR4etri1s7hbuzjtGe5d1WNywYHHzHJPJ/yK1qK9COHjGSkn1b6dfl/XW56sMLCE1NPZyfT7W/T+utwooorpOsKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooqrNqVpb6hDZTTbLicExqVOGx74x+GamUoxV5OxEpxgrydv8AglqiqsOp2lxqE1lDNvuIADKoU4XPvjH4Zq1RGUZq8XcIzjNXi7/8AKKKKosKKKpahqsGmy2iTrIxu5lhTYAcMe556VE5xhHmk7IipUhTjzTdkXaKiurqGytZLm5fZFGNztgnA+gqlHrtnNqNrZw+Y7XUHnxyBcKV988549KmVanBqMnr/mROvSpyUZSSbtp66L8TSoqlqmqwaRbRzXKyMskqxARgE5P1I44qW+v7bTbRrm9k8qFSAW2k4ycdBzTdWmm03tv5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AckUAfSemeI9E1uaaHRtY0/UJYP9alpdJK0fb5gpOPxptj4n0DVJUi0zXNNvJJIjOiW93HIWjB2lwATlQeCemeK+f/g/pWjz/EfRL/SfE8moXVnbSx3Nna+F1sEhBiYFZ5VIDENjBIYkgc96h8J+EluP2T9T1Lw7paP4hvI5Ue5ij3TyQi4USRg9dpjQjaOvPc0Ae7al410xPDeqan4evdM1qXTkLSQR6nDGgbPR5SSsfflvSrS+K9KttO0ybXNR07SrjUIUkjt5r6P5mZQSqNkCTBOMrwa8TuNT+H+pfB/xGPAukm1vbfQBFezJZtCFO5cxyMQA8mec89DzWD49/sjTZtD1MmG71dvD9nbjRdW0l7mG+Qov+olUZjcZI6qc9+eQD6T1XxDouheV/ber2Gm+ccR/bLlIt59BuIzS6j4g0bSLaG41bVrGxgn4ilublI1k/wB0sQD17V80/EKzZvipeXfjPUv+EZsLzS7VbBrvQV1WMfulDwruB2OH38jnvkcUeJdN0fw54R8JXFxqk017YadMtlDr+gNJbaijTSFYimXMT4xgk/d2HI7AH1KjrJGrxsHRgCrKcgj1FLXA+E/G9nbR+D/C13o15pmo6lpCzw2yRlobVI0+4zMdw4XgEE9ATk131ABRRRQAUUUUAFFFFABRRRQAUUUUAYWu+EbDxBruh6tey3CT6HO89ssTKFZmUAhwQSRx2IrdoooAKz9f0W28R+Hb/Rr55Utr+3e3laEgOqsMEgkEZ+oNaFFAFLRdKg0LQdP0izaRrfT7aO1iaUgsURQoJIAGcD0FXaKKACiiigAooooAKKKKACiiigAooooAKKKKAOU8Z/DzS/G1xp93eXmpadf6aXNrfaZdeRNFvxuAOCOcDtn86l8G+A9J8ERXp02W8vLvUJBJeX2oT+dPcMM43NgZxk9u5rpqKAMfxV4X0zxl4budD1yN5LO527xG5RgVYMCCO4IBrnvDXwo0jw74hg1yfVdc13UbWJorWfWb77QbZWGCE4GMgkfia7migAqjrelJrmg3ulS3Nxax3kLQPNbMFkRWGDtJBAOO+KvUUAZnhzQLHwt4bsdD0pWFpYxCKPeQWb1ZiAASSSTwOTWnRRQAUUUUAFFFFABRRRQAUUUUAFFFFABRRRQB5evwC8Lrm2/tPxAdHM3nHRDqR+xFs5+5jPX/AGs+9enqqooVAFVRgADAApaKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigAooooAKKKKACiiigD/2Q==\n",
      "text/plain": [
       "<IPython.core.display.Image object>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "from IPython.display import display, Image\n",
    "\n",
    "# if predict[0]==0:\n",
    "if 0==0:\n",
    "    print(\"Result:\")\n",
    "    display(Image(filename='Datasets/pos.jpg'))\n",
    "else:\n",
    "    print(\"Result:\")\n",
    "    display(Image(filename='Datasets/neg.jpg'))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'predict' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "\u001b[1;32m<ipython-input-4-e4c1f4c2de92>\u001b[0m in \u001b[0;36m<module>\u001b[1;34m\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[1;32mfrom\u001b[0m \u001b[0msklearn\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mlinear_model\u001b[0m \u001b[1;32mimport\u001b[0m \u001b[0mLinearRegression\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      2\u001b[0m \u001b[0mregressor\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mLinearRegression\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[1;32m----> 3\u001b[1;33m \u001b[0mregressor\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mpredict\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0m\u001b[0;32m      4\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mdump\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mregressor\u001b[0m\u001b[1;33m,\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'model.pkl'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'wb'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n\u001b[0;32m      5\u001b[0m \u001b[0mmodel\u001b[0m \u001b[1;33m=\u001b[0m \u001b[0mpickle\u001b[0m\u001b[1;33m.\u001b[0m\u001b[0mload\u001b[0m\u001b[1;33m(\u001b[0m\u001b[0mopen\u001b[0m\u001b[1;33m(\u001b[0m\u001b[1;34m'model.pkl'\u001b[0m\u001b[1;33m,\u001b[0m\u001b[1;34m'rb'\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m)\u001b[0m\u001b[1;33m\u001b[0m\u001b[1;33m\u001b[0m\u001b[0m\n",
      "\u001b[1;31mNameError\u001b[0m: name 'predict' is not defined"
     ]
    }
   ],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "regressor = LinearRegression()\n",
    "regressor.fit(predict)\n",
    "pickle.dump(regressor,open('model.pkl','wb'))\n",
    "model = pickle.load(open('model.pkl','rb'))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Thank You...."
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
