# ``WKInternalsNotes/WKVisibilityPropagationView/stopPropagatingVisibilityToProcess(_:)``

指定プロセスへの可視性伝播を停止する。

## Objective-C Declaration
```objective-c
- (void)stopPropagatingVisibilityToProcess:(WebKit::AuxiliaryProcessProxy&)process;
```

## Discussion
対象プロセスに紐づく interaction を削除し、追跡リストから除去する。

## References
- [`WKVisibilityPropagationView.h#L39`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVisibilityPropagationView.h#L39)
- [`WKVisibilityPropagationView.mm#L66`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVisibilityPropagationView.mm#L66)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
