# ``WKInternalsNotes/WKVisibilityPropagationView/propagateVisibilityToProcess(_:)``

指定プロセスへ可視性を伝播する。

## Objective-C Declaration
```objective-c
- (void)propagateVisibilityToProcess:(WebKit::AuxiliaryProcessProxy&)process;
```

## Discussion
既存の interaction がない場合に、extension process から可視性伝播用 interaction を生成して追加する。

## References
- [`WKVisibilityPropagationView.h#L38`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVisibilityPropagationView.h#L38)
- [`WKVisibilityPropagationView.mm#L45`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/ios/WKVisibilityPropagationView.mm#L45)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-30 |
