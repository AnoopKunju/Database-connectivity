#include "login.h"
int main (void)
{
	int lv_ret;
	char *lp_action = NULL;
	char *lp_userid;
	Form lv_Anooplogin;
	char lv_db_watchlist[50];
	long lv_db_watchid ;
	lv_Anooplogin.handleInput();
	char *lp_firstname = NULL;
	char lv_sql[256]= {""};
	char lv_sqlWl[256]= {""};
	char lv_db_status[50]= {""};
	int	 lv_count = 0;
	char lv_detailsWL[256]={""};
	char log[512] ={""};
	char *lp_status =NULL;
	CKSDbLib lv_sql_db;



	char	lv_db_security[20],
			lv_db_me[3],
			lv_db_tradesmart[10],
			lv_db_it[2],
			lv_db_opttype[10],
			lv_db_cas[2];
    long	lv_db_exchangecode,
			lv_db_expirydate,
			lv_db_ot;
    double	lv_db_strikeprice,
			lv_db_openprice,
			lv_db_lastprice,
			lv_db_highprice,
			lv_db_lowprice,
			lv_db_percentchange,
			lv_db_netchange;


	lp_action = lv_Anooplogin.getValue("action");
	write_debug_log("Anooplogin",lp_action);

	if( lp_action && strcmp(lp_action,"doLogin") == 0)
	{

		lp_firstname = lv_Anooplogin.getValue("firstname");
		write_debug_log("Anooplogin","you are into doLogin");
		write_debug_log("Anooplogin",lp_firstname);
		
		lp_status = lv_Anooplogin.getValue("status");
		write_debug_log("AnoopLogin",lp_status);

		lv_sql_db.SetEnvVariables();//TODO
		//Open connection
		lv_ret = lv_sql_db.SQL_openConnection("172.24.2.150","itrade","web","web@123",1433);
		if(lv_ret != OPEN_CONNECT_SUCCESS) //if not connected properly, show error on FE
		{
                /* Hadnle Error condition Here */
				printf("Connection Error");
                lv_sql_db.closeConnection();
                return 0;
		}

		
        
		sprintf_s(lv_sql,256,"prc_get_user_details '%s'", lp_firstname);  //make ur DB Query
		write_debug_log("AnoopLogin",lv_sql);

		lv_ret = lv_sql_db.getResults(lv_sql);
			if(lv_ret != QRY_EXECUTE_SUCCESS)
				{
					//show error
					lv_sql_db.closeConnection();
					return 0;
				}

			if( lv_sql_db.RecordSet->RecordCount > 0)
				{
					while(VARIANT_TRUE != lv_sql_db.RecordSet->EndOfFile)
						{
                                strcpy_s(lv_db_status,10, ((char *)((_bstr_t)lv_sql_db.RecordSet->Fields->GetItem("status")->Value)));
								write_debug_log("AnoopLogin","status from DB");
								write_debug_log("AnoopLogin",lv_db_status);
								
								lv_sql_db.RecordSet->MoveNext();
						}
				}

			if(strcmpi(lp_status,lv_db_status)==0)
				{
						Form::writeHtmlArgs("/itrade/rsps/Anoop/AnoopWatchList.rsp",NULL);
						sprintf_s(lv_sqlWl, 256,"prc_get_portfolio_master '%s'", lp_firstname);
						write_debug_log("AnoopLogin",lv_sqlWl);
						

						lv_ret = lv_sql_db.getResults(lv_sqlWl);
						if( lv_sql_db.RecordSet->RecordCount > 0)
						{
							while(VARIANT_TRUE != lv_sql_db.RecordSet->EndOfFile)
							{
								write_debug_log("AnoopLogin","in while");
								lv_count++ ; 
								lv_db_watchid = atol(((char *)((_bstr_t)lv_sql_db.RecordSet->Fields->GetItem("portfolio_mast_id")->Value)));
								strcpy_s(lv_db_watchlist,50, ((char *)((_bstr_t)lv_sql_db.RecordSet->Fields->GetItem("portfolio_name")->Value)));
					
								write_debug_log("AnoopLogin", lv_db_watchlist);
								sprintf_s(log,512,"%lf",lv_db_watchid);
								write_debug_log("AnoopLogin",lv_db_watchlist);
									printf("<td> %d </td>",lv_count);
									printf("<td> %ld </td>",lv_db_watchid);
									printf("<td> <a href='Anooplogin.exe?action=show_watch&watch_id=%ld&watch_name=%s'>%s </a> </td>",lv_db_watchid,lv_db_watchlist,lv_db_watchlist);
									printf("</tr>");

								lv_sql_db.RecordSet->MoveNext();
						
							}
				
						}
							//strcpy_s(lv_db_watchlist, 256, ((char *)((_bstr_t)lv_sql_db.RecordSet->Fields->GetItem("portfolio_name")->Value)));
							write_debug_log("AnoopLogin", lv_db_watchlist);

							printf("</table>");
							printf("<input type='hidden' name='uid' id='uid' value=%s",lp_firstname);
							printf("</body></html>");
							return 0;		// one new RSP, SHow a greeting
				}
				else
				{
						Form::writeHtmlArgs("/itrade/rsps/Anoop/AnoopError.rsp",NULL);
						return 0;			//error msg, don’t allow user to login
				}

		}
		
		if(lp_action && strcmp(lp_action,"show_watch")==0)//for carrying out the action further 
		{
			char *lp_uid = NULL;
			lp_uid = lv_Anooplogin.getValue("uid");
			write_debug_log("AnoopLogin","lp_uid in show_watch");
			write_debug_log("AnoopLogin",lp_uid);

			Form::writeHtmlArgs("/itrade/rsps/Anoop/AnoopWlDetails.rsp",NULL);
			sprintf_s(lv_detailsWL, 256,"prc_get_watch_details ,'%s','%ld','%d'", lp_uid,lv_db_watchid,0);// showing the details of the watchlist
			write_debug_log("AnoopLogin","Deatils_WL");
			lv_ret = lv_sql_db.getResults(lv_detailsWL);
			if(lv_sql_db.RecordSet->RecordCount >0 )
			{
				while(VARIANT_TRUE	!= lv_sql_db.RecordSet->EndOfFile)
				{
					strcpy_s(lv_db_security,10,((char *)((_bstr_t)lv_sql_db.RecordSet->Fields->GetItem("Security")->Value)));
					write_debug_log("AnoopLogin","status from DB");
					write_debug_log("AnoopLogin",lv_db_security);
					strcpy_s(lv_db_me,10,((char *)((_bstr_t)lv_sql_db.RecordSet->Fields->GetItem("ME")->Value)));

					printf("<td> %s </td>",lv_db_security);
					printf("<td> %s </td>",lv_db_me);
					printf("</tr>");
				}

				lv_sql_db.RecordSet->MoveNext();
				printf("</table></body></html>");
				write_debug_log("AnoopLogin","in show_watch");
				return 0;
			}
			
		}
	else
	{		
		Form::writeHtmlArgs("/itrade/rsps/Anoop/AnoopLogin.rsp",NULL);
		return 0;
	}

}


