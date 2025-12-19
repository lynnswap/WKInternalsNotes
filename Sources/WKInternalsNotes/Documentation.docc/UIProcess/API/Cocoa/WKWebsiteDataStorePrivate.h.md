# ``WKInternalsNotes/WKWebsiteDataStore``

## Topics

### WKPrivate

#### Properties
- ``WKInternalsNotes/WKWebsiteDataStore/_allowsCellularAccess``
- ``WKInternalsNotes/WKWebsiteDataStore/_allowsTLSFallback``
- ``WKInternalsNotes/WKWebsiteDataStore/_boundInterfaceIdentifier``
- ``WKInternalsNotes/WKWebsiteDataStore/_configuration``
- ``WKInternalsNotes/WKWebsiteDataStore/_delegate``
- ``WKInternalsNotes/WKWebsiteDataStore/_identifier``
- ``WKInternalsNotes/WKWebsiteDataStore/_perOriginStorageQuota``
- ``WKInternalsNotes/WKWebsiteDataStore/_persistedSites``
- ``WKInternalsNotes/WKWebsiteDataStore/_proxyConfiguration``
- ``WKInternalsNotes/WKWebsiteDataStore/_resourceLoadStatisticsDebugMode``
- ``WKInternalsNotes/WKWebsiteDataStore/_resourceLoadStatisticsEnabled``
- ``WKInternalsNotes/WKWebsiteDataStore/_storageSiteValidationEnabled``
- ``WKInternalsNotes/WKWebsiteDataStore/_webPushPartition``

#### Methods
- ``WKInternalsNotes/WKWebsiteDataStore/_abortBackgroundFetch(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_allWebsiteDataTypesIncludingPrivate()``
- ``WKInternalsNotes/WKWebsiteDataStore/_allowTLSCertificateChain(_:forHost:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_allowWebsiteDataRecordsForAllOrigins()``
- ``WKInternalsNotes/WKWebsiteDataStore/_appBoundDomains(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_appBoundSchemes(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_clearLoadedSubresourceDomainsFor(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_clearPrevalentDomain(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_clearResourceLoadStatistics(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_clickBackgroundFetch(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_closeDatabases(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_countNonDefaultSessionSets(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_defaultDataStoreExists()``
- ``WKInternalsNotes/WKWebsiteDataStore/_defaultNetworkProcessExists()``
- ``WKInternalsNotes/WKWebsiteDataStore/_deleteDefaultDataStoreForTesting()``
- ``WKInternalsNotes/WKWebsiteDataStore/_fetchAllIdentifiers(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_fetchDataOfTypes(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_fetchDataRecordsOfTypes(_:withOptions:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_forceNetworkProcessToTaskSuspendForTesting()``
- ``WKInternalsNotes/WKWebsiteDataStore/_getAllBackgroundFetchIdentifiers(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_getAppBadgeForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_getBackgroundFetchState(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_getIsPrevalentDomain(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_getPendingPushMessage(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_getPendingPushMessages(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_getResourceLoadStatisticsDataSummary(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_grantStorageAccessForTesting(_:withSubFrameDomains:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_hasServiceWorkerBackgroundActivityForTesting()``
- ``WKInternalsNotes/WKWebsiteDataStore/_initWithConfiguration(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_isRegisteredAsSubresourceUnderFirstParty(_:thirdParty:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_isRelationshipOnlyInDatabaseOnce(_:thirdParty:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_isStorageSuspendedForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_loadedSubresourceDomainsFor(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_logUserInteraction(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_makeNextNetworkProcessLaunchFailForTesting()``
- ``WKInternalsNotes/WKWebsiteDataStore/_networkProcessExists()``
- ``WKInternalsNotes/WKWebsiteDataStore/_networkProcessHasEntitlementForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_networkProcessIdentifier()``
- ``WKInternalsNotes/WKWebsiteDataStore/_originDirectoryForTesting(_:topOrigin:type:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_pauseBackgroundFetch(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_processPersistentNotificationClick(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_processPersistentNotificationClose(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_processPushMessage(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_processStatisticsAndDataRecords(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_removeDataStoreWithIdentifier(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_renameOrigin(_:to:forDataOfTypes:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_restoreData(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_resumeBackgroundFetch(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_runningOrTerminatingServiceWorkerCountForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_scheduleCookieBlockingUpdate(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_scopeURL(_:hasPushSubscriptionForTesting:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_sendNetworkProcessDidResume()``
- ``WKInternalsNotes/WKWebsiteDataStore/_sendNetworkProcessPrepareToSuspend(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_sendNetworkProcessWillSuspendImminently()``
- ``WKInternalsNotes/WKWebsiteDataStore/_setBackupExclusionPeriodForTesting(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setCachedProcessSuspensionDelayForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setCompletionHandlerForRemovalFromNetworkProcess(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setNetworkProcessSuspensionAllowedForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setPrevalentDomain(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setPrivateClickMeasurementDebugModeEnabled(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setPrivateTokenIPCForTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setResourceLoadStatisticsTestingCallback(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setResourceLoadStatisticsTimeAdvanceForTesting(_:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setRestrictedOpenerTypeForTesting(_:forDomain:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setServiceWorkerOverridePreferences(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setStorageAccessPromptQuirkForTesting(_:withSubFrameDomains:withTriggerPages:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setThirdPartyCookieBlockingMode(_:onlyOnSitesWithoutUserInteraction:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setUserAgentStringQuirkForTesting(_:withUserAgent:completionHandler:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_setWebPushActionHandler(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_sharedServiceWorkerNotificationManager()``
- ``WKInternalsNotes/WKWebsiteDataStore/_statisticsDatabaseHasAllTables(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_storeServiceWorkerRegistrations(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_synthesizeAppIsBackground(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/_terminateNetworkProcess()``
- ``WKInternalsNotes/WKWebsiteDataStore/_trustServerForLocalPCMTesting(_:)``
- ``WKInternalsNotes/WKWebsiteDataStore/handleNotificationResponse(_:)``

### WKWebPushHandling

- ``WKInternalsNotes/WKWebsiteDataStore/_handleWebPushAction(_:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKWebsiteDataStorePrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebsiteDataStorePrivate.h) |
