# ``WKInternalsNotes/_WKTextManipulationItem/tokens``

トークン配列を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy) NSArray<_WKTextManipulationToken *> *tokens;
```

## Default Value
`initWithIdentifier:tokens:` などで渡したトークン配列。

## Discussion
保持している `tokens` をそのまま返す。

## References
- [`_WKTextManipulationItem.h#L41`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L41)
- [`_WKTextManipulationItem.mm#L67`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L67)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
