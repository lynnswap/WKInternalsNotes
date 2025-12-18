# ``WKInternalsNotes/WKProcessPool``

WKProcessPool の Objective-C private/testing API をカテゴリ別に整理した一覧。

## Topics

### WKPrivate

#### Properties
- ``WKInternalsNotes/WKProcessPool/_automationDelegate``
- ``WKInternalsNotes/WKProcessPool/_configuration``
- ``WKInternalsNotes/WKProcessPool/_cookieStoragePartitioningEnabled``
- ``WKInternalsNotes/WKProcessPool/_coreLocationProvider``
- ``WKInternalsNotes/WKProcessPool/_downloadDelegate``
- ``WKInternalsNotes/WKProcessPool/_javaScriptConfigurationDirectory``
- ``WKInternalsNotes/WKProcessPool/_pluginLoadClientPolicies``

#### Methods
- ``WKInternalsNotes/WKProcessPool/_addSupportedPlugin(_:named:withMimeTypes:withExtensions:)``
- ``WKInternalsNotes/WKProcessPool/_allProcessPoolsForTesting()``
- ``WKInternalsNotes/WKProcessPool/_automationCapabilitiesDidChange()``
- ``WKInternalsNotes/WKProcessPool/_clearCaptivePortalModeEnabledGloballyForTesting()``
- ``WKInternalsNotes/WKProcessPool/_clearPermanentCredentialsForProtectionSpace(_:)``
- ``WKInternalsNotes/WKProcessPool/_clearSupportedPlugins()``
- ``WKInternalsNotes/WKProcessPool/_clearWebProcessCache()``
- ``WKInternalsNotes/WKProcessPool/_countWebPagesInAllProcessesForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_crashOnMessageCheckFailureForTesting()``
- ``WKInternalsNotes/WKProcessPool/_forceGameControllerFramework()``
- ``WKInternalsNotes/WKProcessPool/_garbageCollectJavaScriptObjectsForTesting()``
- ``WKInternalsNotes/WKProcessPool/_getActivePagesOriginsInWebProcessForTesting(_:completionHandler:)``
- ``WKInternalsNotes/WKProcessPool/_gpuProcessIdentifier()``
- ``WKInternalsNotes/WKProcessPool/_gpuProcessInfo()``
- ``WKInternalsNotes/WKProcessPool/_hasAudibleMediaActivity()``
- ``WKInternalsNotes/WKProcessPool/_hasPrewarmedWebProcess()``
- ``WKInternalsNotes/WKProcessPool/_isJITDisabledInAllRemoteWorkerProcesses(_:)``
- ``WKInternalsNotes/WKProcessPool/_isMetalDebugDeviceEnabledInGPUProcessForTesting()``
- ``WKInternalsNotes/WKProcessPool/_isMetalShaderValidationEnabledInGPUProcessForTesting()``
- ``WKInternalsNotes/WKProcessPool/_isWebProcessSuspended(_:)``
- ``WKInternalsNotes/WKProcessPool/_lockdownModeEnabledGloballyForTesting()``
- ``WKInternalsNotes/WKProcessPool/_makeNextWebProcessLaunchFailForTesting()``
- ``WKInternalsNotes/WKProcessPool/_maximumSuspendedPageCount()``
- ``WKInternalsNotes/WKProcessPool/_networkingProcessInfo()``
- ``WKInternalsNotes/WKProcessPool/_notificationManagerForTesting()``
- ``WKInternalsNotes/WKProcessPool/_numberOfConnectedGameControllerFrameworkGamepadsForTesting()``
- ``WKInternalsNotes/WKProcessPool/_numberOfConnectedGamepadsForTesting()``
- ``WKInternalsNotes/WKProcessPool/_numberOfConnectedHIDGamepadsForTesting()``
- ``WKInternalsNotes/WKProcessPool/_objectForBundleParameter(_:)``
- ``WKInternalsNotes/WKProcessPool/_pluginProcessCount()``
- ``WKInternalsNotes/WKProcessPool/_preconnectToServer(_:)``
- ``WKInternalsNotes/WKProcessPool/_prewarmedProcessIdentifiersForTesting()``
- ``WKInternalsNotes/WKProcessPool/_processCacheCapacity()``
- ``WKInternalsNotes/WKProcessPool/_processCacheSize()``
- ``WKInternalsNotes/WKProcessPool/_registerURLSchemeAsBypassingContentSecurityPolicy(_:)``
- ``WKInternalsNotes/WKProcessPool/_registerURLSchemeAsCanDisplayOnlyIfCanRequest(_:)``
- ``WKInternalsNotes/WKProcessPool/_registerURLSchemeAsSecure(_:)``
- ``WKInternalsNotes/WKProcessPool/_requestWebProcessTermination(_:)``
- ``WKInternalsNotes/WKProcessPool/_resetPluginLoadClientPolicies(_:)``
- ``WKInternalsNotes/WKProcessPool/_seedResourceLoadStatisticsForTestingWithFirstParty(_:thirdParty:shouldScheduleNotification:completionHandler:)``
- ``WKInternalsNotes/WKProcessPool/_serviceWorkerProcessCount()``
- ``WKInternalsNotes/WKProcessPool/_setAllowsSpecificHTTPSCertificate(_:forHost:)``
- ``WKInternalsNotes/WKProcessPool/_setAutomationSession(_:)``
- ``WKInternalsNotes/WKProcessPool/_setCachedProcessLifetimeForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_setCanHandleHTTPSServerTrustEvaluation(_:)``
- ``WKInternalsNotes/WKProcessPool/_setCaptivePortalModeEnabledGloballyForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_setDomainRelaxationForbiddenForURLScheme(_:)``
- ``WKInternalsNotes/WKProcessPool/_setEnableMetalDebugDeviceInNewGPUProcessesForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_setEnableMetalShaderValidationInNewGPUProcessesForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_setLinkedOnOrAfterEverything()``
- ``WKInternalsNotes/WKProcessPool/_setLinkedOnOrAfterEverythingForTesting()``
- ``WKInternalsNotes/WKProcessPool/_setLinkedOnOrBeforeEverythingForTesting()``
- ``WKInternalsNotes/WKProcessPool/_setObject(_:forBundleParameter:)``
- ``WKInternalsNotes/WKProcessPool/_setObjectsForBundleParametersWithDictionary(_:)``
- ``WKInternalsNotes/WKProcessPool/_setPLTResourceDelayIntervalForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_setUseSeparateServiceWorkerProcess(_:)``
- ``WKInternalsNotes/WKProcessPool/_setUsesOnlyHIDGamepadProviderForTesting(_:)``
- ``WKInternalsNotes/WKProcessPool/_setWebProcessCountLimit(_:)``
- ``WKInternalsNotes/WKProcessPool/_sharedProcessPool()``
- ``WKInternalsNotes/WKProcessPool/_terminateAllWebContentProcesses()``
- ``WKInternalsNotes/WKProcessPool/_terminateServiceWorkers()``
- ``WKInternalsNotes/WKProcessPool/_warmInitialProcess()``
- ``WKInternalsNotes/WKProcessPool/_webContentProcessInfo()``
- ``WKInternalsNotes/WKProcessPool/_webPageContentProcessCount()``
- ``WKInternalsNotes/WKProcessPool/_webProcessCount()``
- ``WKInternalsNotes/WKProcessPool/_webProcessCountIgnoringPrewarmed()``
- ``WKInternalsNotes/WKProcessPool/_webProcessCountIgnoringPrewarmedAndCached()``
- ``WKInternalsNotes/WKProcessPool/_websiteDataURLForContainerWithURL(_:)``
- ``WKInternalsNotes/WKProcessPool/_websiteDataURLForContainerWithURL(_:bundleIdentifierIfNotInContainer:)``

### WKPrivateMac

- ``WKInternalsNotes/WKProcessPool/_registerAdditionalFonts(_:)``

### Class Extension

#### Properties
- ``WKInternalsNotes/WKProcessPool/_geolocationProvider``

#### Methods
- ``WKInternalsNotes/WKProcessPool/_initWithConfiguration(_:)``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKProcessPoolPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKProcessPoolPrivate.h) |
