// src/services/api.ts

export const fetchHelloWorld = async (): Promise<string> => {
    const response = await fetch('/api/');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.text();
    return data;
};

export const fetchLatestDataById = async (damId: string): Promise<any> => {
    const response = await fetch(`/api/latestdata/${damId}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
};

export const fetchDamsDataByGroup = async (groupName: string): Promise<any[]> => {
    const response = await fetch(`/api/damsdata/${groupName}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
};

export const fetchDamNames = async (): Promise<string[]> => {
    const response = await fetch('/api/damnames');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
};

export const fetchDamDataByName = async (damName: string): Promise<any> => {
    const response = await fetch(`/api/damdata?dam_name=${encodeURIComponent(damName)}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
};

export const fetchDamResources = async (damId: string): Promise<any[]> => {
    const response = await fetch(`/api/damresources/${damId}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
};

export const fetchAvgPercentageFull12Months = async (): Promise<number> => {
    const response = await fetch('/api/average_percentage_full/12_months');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.avg_percentage_full_12_months;
};

export const fetchAvgPercentageFull5Years = async (): Promise<number> => {
    const response = await fetch('/api/average_percentage_full/5_years');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.avg_percentage_full_5_years;
};

export const fetchAvgPercentageFull20Years = async (): Promise<number> => {
    const response = await fetch('/api/average_percentage_full/20_years');
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.avg_percentage_full_20_years;
};

export const fetchAvgPercentageFull12MonthsById = async (damId: string): Promise<number> => {
    const response = await fetch(`/api/average_percentage_full/${damId}/12_months`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.avg_percentage_full_12_months;
};

export const fetchAvgPercentageFull5YearsById = async (damId: string): Promise<number> => {
    const response = await fetch(`/api/average_percentage_full/${damId}/5_years`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.avg_percentage_full_5_years;
};

export const fetchAvgPercentageFull20YearsById = async (damId: string): Promise<number> => {
    const response = await fetch(`/api/average_percentage_full/${damId}/20_years`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data.avg_percentage_full_20_years;
};

export const fetchDamData12Months = async (groupName: string): Promise<any[]> => {
    const response = await fetch(`/api/damdata/12_months/${groupName}`);
    if (!response.ok) {
        throw new Error('Network response was not ok');
    }
    const data = await response.json();
    return data;
};
