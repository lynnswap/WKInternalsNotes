# ``WKInternalsNotes/WKFrameInfo/_documentIdentifier``

ドキュメント識別用の NSUUID を返す。

## Objective-C Declaration
```objective-c
@property (nonatomic, readonly, copy, nullable) NSUUID *_documentIdentifier WK_API_AVAILABLE(macos(15.4), ios(18.4), visionos(2.4));
```

## Default Value
`_frameInfo->documentID()->object().createNSUUID()` の結果。

## Discussion
API::FrameInfo の documentID から `NSUUID` を生成して返す。

## References
- [`WKFrameInfoPrivate.h#L36`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfoPrivate.h#L36)
- [`WKFrameInfo.mm#L110`](https://github.com/WebKit/WebKit/blob/WebKit-7623.1.14.10.9/Source/WebKit/UIProcess/API/Cocoa/WKFrameInfo.mm#L110)

## Metadata
| Key | Value |
| --- | ----- |
| Status | Draft |
| Last updated | 2025-12-19 |
