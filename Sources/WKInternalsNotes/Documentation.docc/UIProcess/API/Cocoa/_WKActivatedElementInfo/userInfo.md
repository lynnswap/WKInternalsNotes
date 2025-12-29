# ``WKInternalsNotes/_WKActivatedElementInfo/userInfo``

ユーザー情報辞書を返す（iOS）。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly) NSDictionary *userInfo WK_API_AVAILABLE(ios(11.0));
```

## Default Value
`nil`。

## Discussion
内部初期化時に `userInfo` をコピーして保持し、その値を返す。

## References
- [`_WKActivatedElementInfo.h#L57`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.h#L57)
- [`_WKActivatedElementInfo.mm#L228`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKActivatedElementInfo.mm#L228)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
