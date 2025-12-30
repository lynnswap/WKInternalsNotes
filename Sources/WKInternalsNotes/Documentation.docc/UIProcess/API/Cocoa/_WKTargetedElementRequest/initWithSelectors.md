# ``WKInternalsNotes/_WKTargetedElementRequest/initWithSelectors(_:)``

セレクタ集合を指定して初期化する。

## Objective-C Declaration
```objective-c
- (instancetype)initWithSelectors:(NSArray<NSSet<NSString *> *> *)selectors;
```

## Discussion
`[self init]` 後に `NSArray<NSSet<NSString *>>` を `TargetedElementSelectors` へ変換し、`_request->setSelectors` で設定する。

## References
- [`_WKTargetedElementRequest.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.h#L39)
- [`_WKTargetedElementRequest.mm#L75`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/_WKTargetedElementRequest.mm#L75)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
