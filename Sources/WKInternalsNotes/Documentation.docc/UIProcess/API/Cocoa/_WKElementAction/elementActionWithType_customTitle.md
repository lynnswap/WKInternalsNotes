# ``WKInternalsNotes/_WKElementAction/elementActionWithType(_:customTitle:)``

タイプとカスタムタイトルでアクションを作成する。

## Objective-C Declaration
```objective-c
+ (instancetype)elementActionWithType:(_WKElementActionType)type customTitle:(NSString *)title;
```

## Discussion
内部の `_elementActionWithType:customTitle:assistant:` を `assistant:nil` で呼び出す。

## References
- [`_WKElementAction.h#L69`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L69)
- [`_WKElementAction.mm#L252`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L252)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
