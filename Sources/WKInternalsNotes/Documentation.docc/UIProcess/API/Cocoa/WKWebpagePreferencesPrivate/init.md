# ``WKInternalsNotes/WKWebpagePreferences/init(_:)``

`WebPage.NavigationPreferences` を `WKWebpagePreferences` に反映する。

## Swift Declaration
```swift
convenience init(_ wrapped: WebPage.NavigationPreferences)
```

## Discussion
`preferredContentMode` と `preferredHTTPSNavigationPolicy` は `WebPage.NavigationPreferences` の値を Swift extension の `init(_:)` で変換して設定する。`allowsContentJavaScript` を直接転写し、`backingIsLockdownModeEnabled` が存在し現在値と異なる場合のみ `isLockdownModeEnabled` を更新する。

## References
- [WKWebpagePreferences+Extras.swift#L29](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences+Extras.swift#L29)
- [WKWebpagePreferences+Extras.swift#L40](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences+Extras.swift#L40)
- [WKWebpagePreferences+Extras.swift#L53](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebpagePreferences+Extras.swift#L53)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
