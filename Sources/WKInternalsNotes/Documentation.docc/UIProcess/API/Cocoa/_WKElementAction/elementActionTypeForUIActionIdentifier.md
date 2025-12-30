# ``WKInternalsNotes/_WKElementAction/elementActionTypeForUIActionIdentifier(_:)``

`UIActionIdentifier` からアクション種別を返す。

## Objective-C Declaration
```objective-c
+ (_WKElementActionType)elementActionTypeForUIActionIdentifier:(UIActionIdentifier)identifier WK_API_AVAILABLE(macos(10.15), ios(13.0));
```

## Discussion
識別子の一致を順に判定して種別へ変換し、未知の識別子は `_WKElementActionTypeCustom` を返す。

## References
- [`_WKElementAction.h#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.h#L75)
- [`_WKElementAction.mm#L423`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKElementAction.mm#L423)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
