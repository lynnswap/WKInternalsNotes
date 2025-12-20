# ``WKInternalsNotes/WKWebViewConfiguration/init(_:)``

`WebPage.Configuration` から `WKWebViewConfiguration` を構築する。

## Swift Declaration
```swift
convenience init(_ wrapped: WebPage.Configuration)
```

## Discussion
`wrapped` の設定を `WKWebViewConfiguration` に順次転写する。`websiteDataStore` / `userContentController` / `webExtensionController` をセットし、`defaultWebpagePreferences` は `WebPage.NavigationPreferences` から `WKWebpagePreferences` を生成して入れる。続いて user agent / app-bound / HTTPS upgrade / incremental rendering / inline predictions / adaptive image glyph / `_loadsSubresources` を反映する。

プラットフォーム条件付きで `showsSystemScreenTimeBlockingView`（visionOS 以外）、iOS の `dataDetectorTypes` / `ignoresViewportScaleLimits` / `allowsInlineMediaPlayback`（`mediaPlaybackBehavior` が `automatic` 以外の場合のみ）、macOS の `userInterfaceDirectionPolicy` を設定し、最後に `urlSchemeHandlers` を `WKURLSchemeHandlerAdapter` でラップして登録する。

## References
- [WKWebViewConfiguration+Extras.swift#L30](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L30)
- [WKWebViewConfiguration+Extras.swift#L33](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L33)
- [WKWebViewConfiguration+Extras.swift#L37](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L37)
- [WKWebViewConfiguration+Extras.swift#L39](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L39)
- [WKWebViewConfiguration+Extras.swift#L47](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L47)
- [WKWebViewConfiguration+Extras.swift#L51](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L51)
- [WKWebViewConfiguration+Extras.swift#L60](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L60)
- [WKWebViewConfiguration+Extras.swift#L64](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration+Extras.swift#L64)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
