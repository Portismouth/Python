#1
SELECT SUM(amount) AS total_revenue_3_2012
FROM billing
WHERE charged_datetime LIKE '%2012-03%';

#2
SELECT SUM(amount) AS total_revenue_client_2
FROM billing
	JOIN clients ON clients.client_id = billing.billing_id
WHERE clients.client_id = 2;

#3
SELECT sites.domain_name AS sites_owned_client_10
FROM sites
WHERE sites.client_id = 10;

#4
SELECT domain_name, DATE_FORMAT(created_datetime, "%m") AS month, DATE_FORMAT(created_datetime, "%Y") AS year
FROM sites
GROUP BY month;

#5
SELECT COUNT(leads.leads_id)
FROM leads
WHERE registered_datetime 
	BETWEEN '2011-01-01%' AND '2011-02-15%';
    
#6
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_leads
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id -- no left join here
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-12-31'
GROUP BY clients.client_id;

#7
SELECT CONCAT(clients.first_name, ' ', clients.last_name) AS client_name, COUNT(leads.leads_id) AS num_leads, DATE_FORMAT(leads.registered_datetime, '%M') AS 'month'
FROM clients
	LEFT JOIN sites ON clients.client_id = sites.client_id
    JOIN leads ON sites.site_id = leads.site_id
WHERE leads.registered_datetime BETWEEN '2011-01-01' AND '2011-06-30'
GROUP BY clients.client_id, MONTH(leads.registered_datetime)
ORDER BY MONTH(leads.registered_datetime);
