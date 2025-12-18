# ``WKInternalsNotes/WKNavigationAction/_userInitiatedAction``

ユーザー操作情報を表す _WKUserInitiatedAction を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) _WKUserInitiatedAction *_userInitiatedAction WK_API_AVAILABLE(macos(10.12), ios(10.0));
```

## Default Value
`_navigationAction->protectedUserInitiatedAction()` をラップした結果。

## Discussion
`protectedUserInitiatedAction()` の参照を Objective-C ラッパーに変換して返す。値が無い場合は `nil` になる。

## References
- [`WKNavigationActionPrivate.h#L54`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L54)
- [`WKNavigationAction.mm#L217`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L217)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
