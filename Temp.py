# Plot the temperature data
plt.figure(figsize=(10, 5))
plt.plot(weather_data['Date'], weather_data['Temp'], label='Daily Temperature')
plt.axhline(y=30, color='r', linestyle='--', label='Heatwave Threshold')
plt.xlabel('Date')
plt.ylabel('Temperature (C)')
plt.title('Daily Temperatures')
plt.legend()
plt.show()

# Show the number of heatwave days per year
heatwave_days_per_year = weather_data.groupby('Year')['Heatwave'].sum()
heatwave_days_per_year.plot(kind='bar', figsize=(10, 5), title='Heatwave Days per Year')
plt.xlabel('Year')
plt.ylabel('Number of Heatwave Days')
plt.show()
