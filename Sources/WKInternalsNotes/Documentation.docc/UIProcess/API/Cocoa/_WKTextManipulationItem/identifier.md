# ``WKInternalsNotes/_WKTextManipulationItem/identifier``

項目の識別子を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, nullable, copy) NSString *identifier;
```

## Default Value
`initWithIdentifier:tokens:` などで渡した識別子。

## Discussion
保持している `identifier` をそのまま返す。

## References
- [`_WKTextManipulationItem.h#L40`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.h#L40)
- [`_WKTextManipulationItem.mm#L62`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextManipulationItem.mm#L62)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-20 |
