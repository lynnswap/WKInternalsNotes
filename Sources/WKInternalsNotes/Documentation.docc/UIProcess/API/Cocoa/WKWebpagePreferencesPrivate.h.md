# ``WKInternalsNotes/WKWebpagePreferences``

WKWebpagePreferences の Objective-C private/testing API をカテゴリ別に整理した一覧。

## Topics

### WKPrivate

#### Properties
- ``WKInternalsNotes/WKWebpagePreferences/_activeContentRuleListActionPatterns``
- ``WKInternalsNotes/WKWebpagePreferences/_allowPrivacyProxy``
- ``WKInternalsNotes/WKWebpagePreferences/_allowSharedProcess``
- ``WKInternalsNotes/WKWebpagePreferences/_allowSiteSpecificQuirksToOverrideCompatibilityMode``
- ``WKInternalsNotes/WKWebpagePreferences/_allowedAutoplayQuirks``
- ``WKInternalsNotes/WKWebpagePreferences/_allowsJSHandleCreationInPageWorld``
- ``WKInternalsNotes/WKWebpagePreferences/_alternateRequest``
- ``WKInternalsNotes/WKWebpagePreferences/_applicationNameForUserAgentWithModernCompatibility``
- ``WKInternalsNotes/WKWebpagePreferences/_autoplayPolicy``
- ``WKInternalsNotes/WKWebpagePreferences/_captivePortalModeEnabled``
- ``WKInternalsNotes/WKWebpagePreferences/_colorSchemePreference``
- ``WKInternalsNotes/WKWebpagePreferences/_contentBlockersEnabled``
- ``WKInternalsNotes/WKWebpagePreferences/_customHeaderFields``
- ``WKInternalsNotes/WKWebpagePreferences/_customNavigatorPlatform``
- ``WKInternalsNotes/WKWebpagePreferences/_customUserAgent``
- ``WKInternalsNotes/WKWebpagePreferences/_customUserAgentAsSiteSpecificQuirks``
- ``WKInternalsNotes/WKWebpagePreferences/_deviceOrientationAndMotionAccessPolicy``
- ``WKInternalsNotes/WKWebpagePreferences/_enhancedSecurityEnabled``
- ``WKInternalsNotes/WKWebpagePreferences/_modalContainerObservationPolicy``
- ``WKInternalsNotes/WKWebpagePreferences/_mouseEventPolicy``
- ``WKInternalsNotes/WKWebpagePreferences/_networkConnectionIntegrityEnabled``
- ``WKInternalsNotes/WKWebpagePreferences/_networkConnectionIntegrityPolicy``
- ``WKInternalsNotes/WKWebpagePreferences/_popUpPolicy``
- ``WKInternalsNotes/WKWebpagePreferences/_pushAndNotificationAPIEnabled``
- ``WKInternalsNotes/WKWebpagePreferences/_userContentController``
- ``WKInternalsNotes/WKWebpagePreferences/_visibilityAdjustmentSelectors``
- ``WKInternalsNotes/WKWebpagePreferences/_visibilityAdjustmentSelectorsIncludingShadowHosts``
- ``WKInternalsNotes/WKWebpagePreferences/_websiteDataStore``

#### Methods
- ``WKInternalsNotes/WKWebpagePreferences/_setContentRuleListsEnabled(_:exceptions:)``

### Class Extension

- ``WKInternalsNotes/WKWebpagePreferences/defaultPreferences``

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
| WebKit revision | [`WebKit-7623.1.14.10.9`](https://github.com/WebKit/WebKit/tree/WebKit-7623.1.14.10.9) |
| Header (WebKit repo-relative path) | [`WKWebpagePreferencesPrivate.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferencesPrivate.h) |
