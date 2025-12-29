# ``WKInternalsNotes/_WKFormInputSession/accessoryViewShouldNotShow``

アクセサリビューの表示を抑止するかを設定/取得する。

## Objective-C Declaration
```objective-c
@property (nonatomic) BOOL accessoryViewShouldNotShow WK_API_AVAILABLE(ios(10.0));
```

## Default Value
`false`。

## Discussion
setter で変更があれば保持して `reloadInputViews` を呼び、getter は保持している値を返す。

## References
- [`WKContentViewInteraction.mm#L817`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L817)
- [`WKContentViewInteraction.mm#L822`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKContentViewInteraction.mm#L822)
- [`_WKFormInputSession.h#L44`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKFormInputSession.h#L44)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-29 |
