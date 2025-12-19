# ``WKInternalsNotes/WKWebpagePreferences/init(_:)``

`WebPage.NavigationPreferences` を `WKWebpagePreferences` に反映する。

## Swift Declaration
```swift
convenience init(_ wrapped: WebPage.NavigationPreferences)
```

## Discussion
`preferredContentMode` / `preferredHTTPSNavigationPolicy` / `allowsContentJavaScript` を転写し、lockdown 状態が指定されていれば `isLockdownModeEnabled` を更新する。

## References
- [WKWebpagePreferences+Extras.swift#L53](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences+Extras.swift#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
