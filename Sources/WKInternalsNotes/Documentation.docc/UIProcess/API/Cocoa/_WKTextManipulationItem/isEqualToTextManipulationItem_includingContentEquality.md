# ``WKInternalsNotes/_WKTextManipulationItem/isEqualToTextManipulationItem(_:includingContentEquality:)``

別の項目と同一かを比較する。

## Objective-C Declaration
```objective-c
- (BOOL)isEqualToTextManipulationItem:(nullable _WKTextManipulationItem *)otherItem includingContentEquality:(BOOL)includingContentEquality;
```

## Discussion
識別子とトークン数を比較し、各トークンを `includingContentEquality` 指定で比較して一致した場合に `YES` を返す。

## References
- [`_WKTextManipulationItem.h#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L45)
- [`_WKTextManipulationItem.mm#L83`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L83)
- [`_WKTextManipulationItem.mm#L88`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L88)
- [`_WKTextManipulationItem.mm#L93`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L93)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
