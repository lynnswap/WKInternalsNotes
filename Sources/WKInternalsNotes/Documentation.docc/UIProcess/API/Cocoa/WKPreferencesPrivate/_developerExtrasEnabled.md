# ``WKInternalsNotes/WKPreferencesPrivate/_developerExtrasEnabled``

Web Inspector などの開発者向け機能を有効/無効にする API

## Objective-C Declaration
```objective-c
@property (nonatomic, setter=_setDeveloperExtrasEnabled:) BOOL _developerExtrasEnabled WK_API_AVAILABLE(macos(10.11), ios(9.0));
```

## Default Value
iOS: `NO` / macOS: `NO`

## Discussion
- この API を使わない場合: UIProcess の `WebInspectorUIProxy::connect` が early return し、Web Inspector を開く経路が無効化される。また `ContextMenuController::showContextMenu` が `addDebuggingItems()` を呼ばない。
- `_developerExtrasEnabled = YES`: `WebInspectorUIProxy::connect` が early return しなくなり Web Inspector を開けるようになる。また `ContextMenuController::showContextMenu` が `addDebuggingItems()` を呼ぶ。さらに WebProcess の `WebPage::updatePreferences` で `showMediaStatsContextMenuItemEnabled` と `trackConfigurationEnabled` が `true` に設定される。
- `_developerExtrasEnabled = NO`: 上記の開発者向け機能が無効化される。

## Details
- WebPreferences key: `DeveloperExtrasEnabled`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferencesPrivate.h#L88)
- [`Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L436`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKPreferences.mm#L436)
- [`Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/Inspector/WebInspectorUIProxy.cpp)
- [`Source/WebCore/page/ContextMenuController.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebCore/page/ContextMenuController.cpp)
- [`Source/WebKit/WebProcess/WebPage/WebPage.cpp`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/WebProcess/WebPage/WebPage.cpp)
- [`Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2374`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WTF/Scripts/Preferences/UnifiedWebPreferences.yaml#L2374) (key: `DeveloperExtrasEnabled`)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
