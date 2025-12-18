# ``WKInternalsNotes/WKNavigationAction/_userInitiated``

ユーザー操作起点のナビゲーションかどうかを返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, getter=_isUserInitiated) BOOL _userInitiated;
```

## Default Value
`_navigationAction->isProcessingUserGesture()` の結果。

## Discussion
ユーザーのジェスチャー処理中かどうかをそのまま返す。

## References
- [`WKNavigationActionPrivate.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L45)
- [`WKNavigationAction.mm#L187`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L187)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
