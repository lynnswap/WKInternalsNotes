# ``WKInternalsNotes/_WKTextExtractionInteractionResult/initWithErrorDescription(_:)``

エラー内容を設定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithErrorDescription:(NSString *)errorDescription;
```

## Discussion
`errorDescription` があれば `WKErrorDomain` / `WKErrorUnknown` で `NSError` を作成し、`NSDebugDescriptionErrorKey` に格納する。

## References
- [`_WKTextExtractionInternal.h#L68`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtractionInternal.h#L68)
- [`_WKTextExtraction.mm#L108`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTextExtraction.mm#L108)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
