# ``WKInternalsNotes/_WKFormInputSession/forceSecureTextEntry``

セキュアテキスト入力を強制するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL forceSecureTextEntry WK_API_AVAILABLE(ios(10.0));
```

## Default Value
`false`。

## Discussion
setter で変更があれば保持して `reloadInputViews` を呼び、getter は保持している値を返す。

## References
- [`WKContentViewInteraction.mm#L831`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L831)
- [`WKContentViewInteraction.mm#L836`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L836)
- [`_WKFormInputSession.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
