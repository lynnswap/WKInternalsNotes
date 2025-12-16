# ``WKInternalsNotes/WKWebViewConfigurationPrivate/_WKDragLiftDelay``

ドラッグ開始（lift）までの遅延プリセット

## Objective-C Declaration
```objective-c
typedef NS_ENUM(NSUInteger, _WKDragLiftDelay) {
    _WKDragLiftDelayShort = 0,
    _WKDragLiftDelayMedium,
    _WKDragLiftDelayLong
} WK_API_AVAILABLE(ios(11.0));
```

## Values
- `_WKDragLiftDelayShort`: UIKit のデフォルト lift delay（`_UIDragInteractionDefaultLiftDelay()`）を使う。
- `_WKDragLiftDelayMedium`: lift delay を `0.5` 秒に設定する。
- `_WKDragLiftDelayLong`: lift delay を `0.65` 秒に設定する。

## Details
- Related property: ``WKInternalsNotes/WKWebViewConfigurationPrivate/_dragLiftDelay``
- Search hint: `WebKitDebugDragLiftDelay`

## References
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L30`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfigurationPrivate.h#L30)
- [`Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKWebViewConfiguration.mm#L75)
- [`Source/WebKit/UIProcess/API/APIPageConfiguration.h`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/APIPageConfiguration.h)
- [`Source/WebKit/UIProcess/API/Cocoa/APIPageConfigurationCocoa.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/APIPageConfigurationCocoa.mm)
- [`Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10553`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L10553)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-16 |
