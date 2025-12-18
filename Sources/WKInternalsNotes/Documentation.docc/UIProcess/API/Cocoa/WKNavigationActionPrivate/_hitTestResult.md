# ``WKInternalsNotes/WKNavigationAction/_hitTestResult``

ヒットテスト結果を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKHitTestResult *_hitTestResult WK_API_AVAILABLE(macos(13.3), ios(16.4));
```

## Default Value
`webHitTestResultData` とページから生成した `_WKHitTestResult`。

## Discussion
`PLATFORM(MAC)` または `HAVE(UIKIT_WITH_MOUSE_SUPPORT)` の場合のみ実行される。`webHitTestResultData` と `page` が揃えば `API::HitTestResult::create` をラップして返し、条件を満たさない場合は `nil`。

## References
- [`WKNavigationActionPrivate.h#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L66)
- [`WKNavigationAction.mm#L260`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L260)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
