# ``WKInternalsNotes/_WKTextManipulationToken/isEqualToTextManipulationToken(_:includingContentEquality:)``

別のトークンと同一かを比較する。

## Objective-C Declaration
```objective-c
- (BOOL)isEqualToTextManipulationToken:(nullable _WKTextManipulationToken *)otherToken includingContentEquality:(BOOL)includingContentEquality;
```

## Discussion
識別子・除外フラグ・`userInfo` を比較し、`includingContentEquality` が `YES` の場合は `content` も比較する。

## References
- [`_WKTextManipulationToken.h#L43`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.h#L43)
- [`_WKTextManipulationToken.mm#L82`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.mm#L82)
- [`_WKTextManipulationToken.mm#L87`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationToken.mm#L87)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
