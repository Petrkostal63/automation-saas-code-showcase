/**
 * Small, framework-independent TypeScript example for a company directory.
 * It is sample domain logic, not the frontend or backend of any private product.
 */
export interface CompanyRecord {
  id: string;
  name: string;
  countryCode: string;
  sector: string;
  confirmedPromotionCents: number;
  currentTotalConfirmedAt: string; // ISO-8601 timestamp
}

export interface DirectoryFilter {
  countryCode?: string;
  sector?: string;
}

export function filterDirectory(
  records: readonly CompanyRecord[],
  filter: DirectoryFilter = {},
): CompanyRecord[] {
  const country = filter.countryCode?.trim().toUpperCase();
  const sector = filter.sector?.trim().toLocaleLowerCase();

  return records.filter((record) => {
    const matchesCountry = !country || record.countryCode.toUpperCase() === country;
    const matchesSector = !sector || record.sector.toLocaleLowerCase() === sector;
    return matchesCountry && matchesSector;
  });
}

/**
 * Promotional ordering only. This is not a company quality, trust, or performance score.
 */
export function sortPromotionalDirectory(
  records: readonly CompanyRecord[],
): CompanyRecord[] {
  return [...records].sort((a, b) => {
    if (a.confirmedPromotionCents !== b.confirmedPromotionCents) {
      return b.confirmedPromotionCents - a.confirmedPromotionCents;
    }
    const timeDelta = Date.parse(a.currentTotalConfirmedAt) - Date.parse(b.currentTotalConfirmedAt);
    if (timeDelta !== 0) return timeDelta;
    return a.id.localeCompare(b.id);
  });
}
