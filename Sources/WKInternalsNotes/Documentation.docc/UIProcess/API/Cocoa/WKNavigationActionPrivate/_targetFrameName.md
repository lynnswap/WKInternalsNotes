# ``WKInternalsNotes/WKNavigationAction/_targetFrameName``

ターゲットフレーム名を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSString *_targetFrameName WK_API_AVAILABLE(macos(14.2), ios(17.2));
```

## Default Value
`_navigationAction->targetFrameName()` の値を `NSString` に変換したもの。

## Discussion
`targetFrameName()` が null の場合は `nil` を返し、非 null の場合は `NSString` に変換して返す。

## References
- [`WKNavigationActionPrivate.h#L50`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationActionPrivate.h#L50)
- [`WKNavigationAction.mm#L280`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKNavigationAction.mm#L280)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
