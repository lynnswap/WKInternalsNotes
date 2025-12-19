# ``WKInternalsNotes/WKNavigation/_userInitiated``

ユーザー操作起点のナビゲーションかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isUserInitiated) BOOL _userInitiated;
```

## Default Value
`_navigation->wasUserInitiated()` の結果。

## Discussion
API::Navigation の `wasUserInitiated()` を呼び、ユーザー起点かどうかを返す。

## References
- [`WKNavigationPrivate.h#L34`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationPrivate.h#L34)
- [`WKNavigation.mm`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigation.mm)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
